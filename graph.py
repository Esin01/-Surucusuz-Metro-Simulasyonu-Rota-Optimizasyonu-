# Gerekli olan kütüphaneler import edildi
import networkx as nx
import matplotlib.pyplot as plt

# Boş bir grafik (Graph) nesnesi oluşturuldu
G = nx.Graph()

def metro_station_graph(G):
    # Düğümler (nodes) eklendi, her düğüm bir isim ve hat bilgisi barındırıyor
    G.add_nodes_from([
        #kırmızı_hat
        ("K1", {"name": "Kızılay", "hat": "Kırmızı Hat"}),
        ("K2", {"name": "Ulus", "hat": "Kırmızı Hat"}),
        ("K3", {"name": "Demetevler", "hat": "Kırmızı Hat"}),
        ("K4", {"name": "OSB", "hat": "Kırmızı Hat"}),

        #mavi_hat
        ("M1", {"name": "Aşti", "hat": "Mavi Hat"}),
        ("M2", {"name": "Kızılay", "hat": "Mavi Hat"}),
        ("M3", {"name": "Sıhhiye", "hat": "Mavi Hat"}),
        ("M4", {"name": "Gar", "hat": "Mavi Hat"}),

        #turuncu_hat
        ("T1", {"name": "Batıkent", "hat": "Turuncu Hat"}),
        ("T2", {"name": "Demetevler", "hat": "Turuncu Hat"}),
        ("T3", {"name": "Gar", "hat": "Turuncu Hat"}),
        ("T4", {"name": "Keçiören", "hat": "Turuncu Hat"}),
    ])

    # Kenarlar (edges) eklendi, her kenar bir ağırlık (weight) barındırıyor
    G.add_edges_from([
        ("K1", "K2", {"weight": 4}),
        ("K2", "K3", {"weight": 6}),
        ("K3", "K4", {"weight": 8}),

        ("M1", "M2", {"weight": 5}),
        ("M2", "M3", {"weight": 3}),
        ("M3", "M4", {"weight": 4}),

        ("T1", "T2", {"weight": 7}),
        ("T2", "T3", {"weight": 9}),
        ("T3", "T4", {"weight": 5}),

        # Aktarma olan hatlar
        ("K1", "M2", {"weight": 2}),
        ("K3", "T2", {"weight": 3}),
        ("M4", "T3", {"weight": 2}),
    ])

    # Hat renkleri
    line_color = {
        "Kırmızı Hat": "red",
        "Turuncu Hat": "orange",
        "Mavi Hat": "blue"
    }

    # Kenar renkleri 
    edge_color = []
    for a, b, c in G.edges(data=True):
        line_a = G.nodes[a]["hat"]
        line_b = G.nodes[b]["hat"]
        # Aynı hatta ait kenarlar (kırmızı hat=kırmızı,mavi hat =mavi, turuncu hat=turuncu) rengine boyanıyor, farklı hatlar gri renkte olacak
        if line_a == line_b:
            edge_color.append(line_color[line_a])
        else:
            edge_color.append("gray")

    # Düğümlerin koordinatları 
    pos_nodes = {
        "K1": (2, 9),
        "K2": (2, 7),
        "K3": (2, 5),
        "K4": (2, 3),

        "M1": (5, 9),
        "M2": (5, 7),
        "M3": (5, 5),
        "M4": (5, 3),

        "T1": (8, 9),
        "T2": (8, 7),
        "T3": (8, 5),
        "T4": (8, 3),
    }

    # Düğüm etiketlerinin pozisyonları(sağ üstte olacak şekilde)
    pos_nodes_attributes = {}
    for node, (x, y) in pos_nodes.items():
        pos_nodes_attributes[node] = (x + 0.5, y + 0.4)

    # Düğüm etiketleri (isim ve hat bilgisi) 
    nodes_labels = {n: (e["name"], e["hat"]) for n, e in G.nodes(data=True)}

    # Kenar etiketleri (ağırlık bilgisi) 
    edges_labels = {(a, b): e["weight"] for a, b, e in G.edges(data=True)}

    # Grafiğin çizimi
    nx.draw(
        G, 
        pos=pos_nodes, 
        with_labels=True, 
        node_color="purple", 
        node_size=1200, 
        font_color="white", 
        font_size=12, 
        font_weight="bold", 
        edge_color=edge_color, 
        width=3
    )

    # Düğüm etiketlerinin çizimi
    nx.draw_networkx_labels(
        G, 
        pos=pos_nodes_attributes, 
        labels=nodes_labels, 
        font_color="black", 
        font_size=10, 
        font_weight="bold"
    )

    # Kenar etiketlerinin çizimi
    nx.draw_networkx_edge_labels(
        G, 
        pos=pos_nodes, 
        edge_labels=edges_labels, 
        label_pos=0.5
    )

    # Grafiği göster
    plt.show()