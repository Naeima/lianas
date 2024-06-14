import csv
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD

# Define namespaces
FOO = Namespace("https://w3id.org/def/foo#")
SOSA = Namespace("http://www.w3.org/ns/sosa/")
GEO = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")

# Create a new graph
g = Graph()

# Bind namespaces
g.bind("foo", FOO)
g.bind("sosa", SOSA)
g.bind("geo", GEO)

# Path to your CSV file
csv_file_path = "lianas.csv"  # Adjust the path accordingly

# Read and process data
with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    # Print headers for debugging
    print("Headers:", reader.fieldnames)

    for row in reader:
        site_name = row.get('Site_name', '').strip()
        plot_no = row.get('Plot_no', '').strip()
        site_plot_code = row.get('Site_plot_code', '').strip()
        date = row.get('Date', '').strip()
        tree_individual_no = row.get('Tree_individual_no', '').strip()
        tree_id = row.get('Tree_ID', '').strip()
        tree_dbh_cm = row.get('Tree_dbh_cm', '').strip()
        tree_height_m = row.get('Tree_height_m', '').strip()
        tree_n_lianas = row.get('Tree_N_lianas', '').strip()
        liana_dbh_cm = row.get('Liana_dbh_cm', '').strip()
        tree_notes = row.get('Tree_notes', '').strip()
        subplot_radius_m = row.get('Subplot_radius_m', '').strip()

        # Create tree observation URI
        tree_observation = URIRef(f"https://w3id.org/def/foo#TreeObservation{tree_individual_no}")

        g.add((tree_observation, RDF.type, FOO.Observation))
        g.add((tree_observation, FOO.SiteName, Literal(site_name, datatype=XSD.string)))
        g.add((tree_observation, FOO.PlotNo, Literal(plot_no, datatype=XSD.integer)))
        g.add((tree_observation, FOO.SitePlotCode, Literal(site_plot_code, datatype=XSD.string)))
        g.add((tree_observation, FOO.Date, Literal(date, datatype=XSD.date)))
        g.add((tree_observation, FOO.TreeIndividualNo, Literal(tree_individual_no, datatype=XSD.integer)))
        g.add((tree_observation, FOO.TreeID, Literal(tree_id, datatype=XSD.string)))
        g.add((tree_observation, FOO.TreeDbhCm, Literal(tree_dbh_cm, datatype=XSD.double)))
        g.add((tree_observation, FOO.TreeHeightM, Literal(tree_height_m, datatype=XSD.double)))
        g.add((tree_observation, FOO.TreeNLianas, Literal(tree_n_lianas, datatype=XSD.integer)))
        g.add((tree_observation, FOO.LianaDbhCm, Literal(liana_dbh_cm, datatype=XSD.double)))
        g.add((tree_observation, FOO.TreeNotes, Literal(tree_notes, datatype=XSD.string)))
        g.add((tree_observation, FOO.SubplotRadiusM, Literal(subplot_radius_m, datatype=XSD.double)))

# Serialize the graph to a file
output_file = "tree_knowledge_graph.ttl"
g.serialize(destination=output_file, format="turtle")

print(f"Knowledge graph has been serialized to {output_file}")
