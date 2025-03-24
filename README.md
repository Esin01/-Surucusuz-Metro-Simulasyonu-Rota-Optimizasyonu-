# Sürücüsüz Metro Simülasyonu Rota Optimizasyonu

## Proje Başlığı ve Kısa Açıklama

Bu proje, sürücüsüz bir metro sisteminin simülasyonunu yaparak, kullanıcılara iki istasyon arasında en az aktarmalı veya en hızlı rotayı bulma imkânı sunar. BFS algoritması ile en az aktarmalı rota bulunurken, A* algoritması ile en hızlı rota hesaplanmaktadır. Grafiksel gösterim için yani (metro istasyonlarını graph veri yapısını kullanarak görselleştirmek için) NetworkX ve Matplotlib kullanılmıştır.

## Kullanılan Teknolojiler ve Kütüphaneler

Proje Python dili ile geliştirilmiştir ve aşağıdaki kütüphaneleri kullanmaktadır:

- **Python:** Temel programlama dili.
- **collections:** `defaultdict` ve `deque` veri yapılarını kullanarak veri saklama ve kuyruk işlemleri için kullanılmıştır.
- **heapq:** A* algoritmasının öncelikli kuyruk yapısının uygulanmasında kullanılmıştır.
- **typing:** Tip ipuçları sağlamak için (Dict, List, Tuple, Optional).
- **networkx:** Metro ağını oluşturmak ve analiz etmek için kullanılmıştır.
- **matplotlib:** Metro ağının görselleştirilmesi için kullanılmıştır.

## Algoritmaların Çalışma Mantığı

### BFS Algoritması (En Az Aktarmalı Rota Bulma)

BFS (Breadth-First Search), bir grafiğin en kısa yollarını bulmada etkili bir algoritmadır. Bu projede, istasyonlar arasındaki en az aktarmalı rotayı bulmak için kullanılmaktadır. Algoritmanın temel işleyişi şu şekildedir:

1. Başlangıç istasyonu bir kuyruk yapısına eklenir.
2. Kuyruktan bir istasyon çıkarılır ve komşu istasyonlar kontrol edilir(gerek olmadığı için ağırlıkları kullanmadık).
3. Daha önce ziyaret edilmemiş olan istasyonlar kuyruğa eklenir.
4. Hedef istasyona ulaşıldığında algoritma durur ve en kısa aktarmalı rota döndürülür.

### A* Algoritması (En Hızlı Rota Bulma)

A* (A Star) algoritması, en hızlı rotayı bulmak için kullanılan sezgisel bir algoritmadır. Algoritma, mevcut mesafe (öğrenilmiş maliyet yani g(n)) ve tahmini mesafeyi (heuristic yani h(n)) birleştirerek en iyi rotayı hesaplar:

1. Başlangıç istasyonu bir öncelikli kuyruğa eklenir.
2. Kuyruktan en düşük maliyetli istasyon çıkarılır.
3. Komşu istasyonların mesafeleri hesaplanarak kuyruğa eklenir.(f(n) hesap edilir yani f(n)=g(n)+h(n))
4. Hedef istasyona ulaşıldığında en hızlı rota bulunmuş olur.

**Neden BFS ve A\* Kullanıldı?**

- **BFS**, en az aktarmalı rotaları bulmamızı sağlar.
- **A***, en hızlı rotayı bulmamızı sağlayan algoritmadır.

## Örnek Kullanım ve Test Sonuçları

1. Program başlatıldığında metro ağının bir görselleştirmesi oluşturulur.
2. Kullanıcı belirli bir başlangıç ve hedef istasyonu girerek iki algoritmayla farklı rotaları test edebilir.
3. Konsol çıktıları aşağıdaki gibi olur:

```
En az aktarmalı rota: K1 -> K5 -> K8
Toplam aktarma sayısı: 2

En hızlı rota: K1 -> K2 -> K5 -> K8
Toplam süre: 12 dakika
```

Bu projeye katılmak veya katkıda bulunmak için GitHub sayfamı ziyaret edebilirsiniz!

https://github.com/Esin01
