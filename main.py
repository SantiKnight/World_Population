import read_csv
import charts
import utils

def run():
    data = read_csv.read_csv('./data.csv')
    labels, values = utils.get_population_porcentile(data)
    charts.generate_pie_chart(labels=labels, values=values)

if __name__ == "__main__":
    run()