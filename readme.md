# Klasifikasi Tweet Banjir API

API untuk mengklasifikasikan tweet terkait banjir menggunakan machine learning.

## Deskripsi

Project ini adalah API yang dibangun untuk mengklasifikasikan tweet terkait banjir. API ini menggunakan model machine learning untuk menganalisis dan mengkategorikan tweet berdasarkan kontennya.

## Fitur

- Klasifikasi tweet banjir menggunakan machine learning
- API endpoints untuk prediksi klasifikasi
- Manajemen model machine learning
- Monitoring dan logging

## Persyaratan Sistem

- Docker

## Instalasi dan Penggunaan

1. Clone repository

```bash
git clone https://github.com/riskihajar/klasifikasi-tweet-banjir-api.git
cd klasifikasi-tweet-banjir-api
```

2. Build Docker image

```bash
docker build -t banjir-api .
```

3. Jalankan container

```bash
docker run -p 8000:8000 banjir-api
```

## Penggunaan API

### Prediksi Klasifikasi

```
POST /predict
```

Contoh request menggunakan curl:

```bash
curl -X POST https://api-banjir.ds.riskihajar.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"banjir besar di kota bandung"}'
```

Response:

```json
{
  "prediction": "klasifikasi",
  "confidence": 0.95
}
```

## Struktur Project

- `main.py` - File utama aplikasi
- `flood_tweet_model.pkl` - Model machine learning
- `requirements.txt` - Dependencies Python
- `Dockerfile` - Konfigurasi Docker
- `templates/` - Template HTML (jika ada)

## Kontribusi

1. Fork project
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## Lisensi

Distribusikan di bawah lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.

## Kontak

Riskihajar - [@riskihajar](https://github.com/riskihajar)

Link Project: [https://github.com/riskihajar/klasifikasi-tweet-banjir-api](https://github.com/riskihajar/klasifikasi-tweet-banjir-api)
