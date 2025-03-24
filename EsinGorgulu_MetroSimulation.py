from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional
import graph

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """
        #Başlangıç ve hedef istasyonlarının varlığını kontrol et(eğer bu duraklardan birisi yoksa none döndür)
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        #Başlangıç ve hedef istasyonlarını al
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic}  # Ziyaret edilen istasyonları takip etmek için bir küme oluşturduk

        kuyruk = deque([(baslangic, [baslangic])])#Başlangıç istasyonunu ve rotayı kuyruğa ekledik(deque kullanarak bfs algoritmasını uyguladık)
        ziyaret_edildi = set() #Ziyaret edilen istasyonları takip etmek için bir set() oluşturduk(çünkü ziyaret edilen istasyonları bir daha ziyaret etmek istemiyoruz) 

        #Kuyruk boş olana kadar döngü çalışacak
        while kuyruk:
            istasyon, rota = kuyruk.popleft()  # Kuyruğun başındaki istasyonu al(en soldaki değeri alır ve listeden çıkarır)
            
            # Hedefe ulaştıysak rotayı döndür
            if istasyon == hedef:
                return rota
            
            # Bulunduğumuz istasyonun daha önceden ziyaret etmediysek ziyaret edildi setine ekle
            if istasyon not in ziyaret_edildi:
                ziyaret_edildi.add(istasyon)
                
                for komsu, _ in istasyon.komsular: # Sadece istasyonu almak için süreyi almamak için("_" kullanmamızın sebebi süreyi göz önüne almamak")
                    if komsu not in ziyaret_edildi:
                        kuyruk.append((komsu, rota + [komsu])) #Komşu istasyon daha önce ziyaret edilmediyse kuyruğa ekle

        # Eğer hedefe ulaşılamadıysa None döndür
        return None  
   


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """
        # Başlangıç ve hedef istasyonlarının varlığını kontrol et(eğer bu duraklardan birisi yoksa none döndür)
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        # Başlangıç ve hedef istasyonlarını al
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set() # Ziyaret edilen istasyonları takip etmek için set yapısını kullandık(çünkü ziyaret edilen istasyonları bir daha ziyaret etmek istemiyoruz)  

        open_list = []  # Öncelik kuyruğu oluşturduk heapq için

        # id eklememin sebebi iki tane nesne karşılaştıralamaz hatası almak için

        # id eklememimizin sebebi iki tane nesne karşılaştıralamaz hatası almamak için(iki yol birbirine eşit olduğu zaman id e bakıp karar veriyor)
        heapq.heappush(open_list, (heuristic_values.get(baslangic_id, 0), 0, id(baslangic), baslangic, []))  # (f, g, id, istasyon, yol)

        # open_list boş olana kadar döngü çalışacak
        while open_list:
            _, g, _, istasyon, rota = heapq.heappop(open_list)  # Kullanmayacaklarımızı _ ile belirttik

            if istasyon in ziyaret_edildi:
                continue  # Eğer istasyon zaten ziyaret edildiyse atla

            rota.append(istasyon)  # İstasyon ziyaret edilmemiş ise rotaya ekle

            # Hedefe ulaştıysak rotayı ve toplam süreyi döndür
            if istasyon is hedef:
                return rota, g

            ziyaret_edildi.add(istasyon)  # Hedefe ulaşmadıysak, ziyaret edildi olarak işaretleriz(yani ziyaret_edildi listesine ekleriz)

            # Komşuları gezeriz ve uygun olanları heapq ya ekleriz
            for komsu, sure in istasyon.komsular: # Bu sefer süre lazım olduğu için "_" kullanmadık
                if komsu in ziyaret_edildi:
                    continue
                
                g_new = g + sure  # g(n)'i güncelledik
                f_new = g_new + heuristic_values.get(komsu.idx, 0)  # h(n) ile g(n)'i toplayarak yeni f(n) değerini buluruz
                heapq.heappush(open_list, (f_new, g_new, id(komsu), komsu, rota[:]))  # Değişikleri heappush ettik

        # Eğer hedefe ulaşamazsak None döndürürüz
        return None

# A* algoritması kullanmak için sezgisel değer oluşturdum
heuristic_values = {
    "K1": 1,
    "K2": 0,
    "K3": 1,
    "K4": 0,

    "M1": 0,
    "M2": 1,
    "M3": 0,
    "M4": 1,

    "T1": 0,
    "T2": 1,
    "T3": 1,
    "T4": 0
}

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 

graph.metro_station_graph(graph.G) #graph.py dosyasındaki oluşturduğumuz fonksiyonu çağırdık