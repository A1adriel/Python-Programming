from jinja2 import Environment, FileSystemLoader
import os


class ViewController:
    def __init__(self, values):
        self.values = values
        self.environment = Environment(
            loader=FileSystemLoader(os.path.join(os.getcwd(), 'templates')))

    def __call__(self):
        if len(self.values) >= 3:
            return f"{self.values[0]} - {self.values[1]} - {self.values[2]}"
        return "No data available"

    def jinja2_view(self):
        template = self.environment.get_template("index.html")
        return template.render(valutes=self.values)
