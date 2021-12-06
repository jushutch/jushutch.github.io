"""Build static HTML site from directory of HTML templates and plain files."""
import json
import shutil
import sys
from pathlib import Path
import click
import jinja2


@click.command()
@click.argument('input_dir',
                type=click.Path(file_okay=False))
@click.option('--output',
              '-o',
              type=click.Path(file_okay=False),
              help='Output directory.',
              metavar='PATH')
@click.option('--verbose',
              '-v',
              is_flag=True,
              help='Print more output.')
def main(input_dir, output, verbose):
    """Templated static website generator."""
    input_dir = Path(input_dir)
    output_directory = input_dir / 'html' if not output else Path(output)
    generator = StaticWebsiteGenerator(
        input_dir=input_dir,
        output_dir=output_directory,
        verbose=verbose)
    generator.generate()


class StaticWebsiteGenerator:
    """A class for generating static websites from templates."""

    def __init__(self, input_dir, output_dir, verbose):
        """Initialize the generator by setting properties and \
        creating jinja2 environment."""
        if not input_dir.exists():
            print(f"The directory {input_dir} does not exist")
            sys.exit(1)
        self.input_dir = input_dir
        if output_dir.exists():
            print(f"The output directory {output_dir} already exists")
            sys.exit(1)
        self.output_dir = output_dir
        self.verbose = verbose
        self.template_dir = input_dir / 'templates'
        self.template_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(str(self.template_dir.resolve())),
            autoescape=jinja2.select_autoescape(['html', 'xml']),
        )
        self.data = self.get_data()

    def generate(self):
        """Copy static files and generate files from templates."""
        try:
            # self.__copy_static_files()
            if not self.output_dir.exists():
                self.output_dir.mkdir()
            self.__generate_from_templates()
        except FileNotFoundError as exception:
            print(f"An exception was thrown trying to find \
                {exception.filename}: {exception}")
            sys.exit(1)
        except jinja2.TemplateError as exception:
            print(f'An exception occurred while rendering: {exception}')
            if self.output_dir.exists():
                shutil.rmtree(self.output_dir)
            sys.exit(1)
        except json.JSONDecodeError as exception:
            print(f"An exception occurded while decoding data.json: \
                {exception}")
            if self.output_dir.exists():
                shutil.rmtree(self.output_dir)
            sys.exit(1)

    def get_data(self):
        """Load the expected data.json."""
        data_file = self.input_dir / 'data.json'
        with open(data_file.resolve(), 'r') as data_file:
            data = json.load(data_file)
        return data

    def __copy_static_files(self):
        static_dir = self.input_dir / 'static'
        if static_dir.exists():
            shutil.copytree(static_dir, self.output_dir/'static')
            if self.verbose:
                print(f'Copied {static_dir} -> {self.output_dir}')

    def __generate_from_templates(self):
        for template in self.data:
            template_file = template['template']
            template_data = template['context']
            url = template['url'].lstrip("/")
            template = self.template_env.get_template(template_file)
            rendered = template.render(template_data)
            output_filename = self.output_dir / url / 'index.html'
            if not output_filename.parent.exists():
                output_filename.parent.mkdir(parents=True)
            with open(output_filename.resolve(), 'w') as output_file:
                output_file.write(rendered)
            if self.verbose:
                print(f'Rendered {template_file} -> {output_filename}')


if __name__ == "__main__":
    main()
