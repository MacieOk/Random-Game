
class HTMLReportGenerator:
    def __init__(self, title="Jeu de Tacquin Report"):

        """
        Initializes the HTMLReportGenerator with a title.
        :param title: The title of the report.
        """

        self.title = title
        self.sections = []

    def add_section(self, header, content)-> None:

        """
        Adds a section to the report.
        :param header: The header of the section.
        :param content: The HTML content of the section.
        """

        self.sections.append({'header': header, 'content': content})

    def add_plot(self, plot_func, *args, **kwargs)-> None:

        """
        Adds a plot to the report by calling the plot function.
        :param plot_func: A function that generates a plot.
        :param args: Arguments to pass to the plot function.
        :param kwargs: Keyword arguments to pass to the plot function.
        """

        plot_filename = kwargs.pop('filename', 'plot.png')
        title = kwargs.pop('title', 'Plot')
        plot_func(*args, **kwargs)
        plt.savefig(plot_filename)
        plt.close()

        img_tag = f'<img src="{plot_filename}" alt="{title}">'
        self.sections.append({'header': title, 'content': img_tag})

    def generate_html(self, output_filename="report.html")-> None:

        """
        Generates the HTML report.
        :param output_filename: The filename for the HTML report.
        """

        template = Template("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{{ title }}</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { text-align: center; }
                .section { margin-bottom: 40px; }
                h2 { color: #333; }
            </style>
        </head>
        <body>
            <h1>{{ title }}</h1>
            {% for section in sections %}
            <div class="section">
                <h2>{{ section.header }}</h2>
                <div>{{ section.content | safe }}</div>
            </div>
            {% endfor %}
        </body>
        </html>
        """)

        html_content = template.render(title=self.title, sections=self.sections)

        with open(output_filename, 'w') as f:
            f.write(html_content)

        print(f"Report generated: {os.path.abspath(output_filename)}")


# Example of use:
if __name__ == "__main__":
    from game_logic import JeuDeTacquin
    results = [(0.1, 3), (0.2, 5), (0.3, 2), (0.4, 6)]

    report = HTMLReportGenerator(title="Jeu de Tacquin Analysis Report")

    report.add_section("Introduction", "<p>This report summarizes the results of the Jeu de Tacquin analysis.</p>")

    table_html = "<table border='1'><tr><th>Start Value</th><th>i-j Difference</th></tr>"
    for start_value, i_j_diff in results:
        table_html += f"<tr><td>{start_value:.2f}</td><td>{i_j_diff}</td></tr>"
    table_html += "</table>"
    report.add_section("Results", table_html)

    def plot_example():
        x_values = [x[0] for x in results]
        y_values = [x[1] for x in results]
        plt.scatter(x_values, y_values)
        plt.xlabel("Start Value")
        plt.ylabel("i-j Difference")
        plt.title("Example Plot")

    report.add_plot(plot_example, filename="example_plot.png", title="i-j Difference vs. Start Value")


    def plot_jeu_de_tacquin():
        random_numbers = [0.5, 0.334, 0.694, 0.543, 0.822, 0.171,
                          0.685, 0.976, 0.809, 0.910, 0.414, 0.856]
        jeu = JeuDeTacquin(random_numbers)
        young_tableau = jeu.insertion_tableau()
        jeu.draw_young_table_with_path(young_tableau, "young_tableau_with_path")

    report.add_plot(plot_jeu_de_tacquin, filename="jeu_de_tacquin_plot.png", title="Jeu de Tacquin Path")

    report.generate_html("example_report.html")
