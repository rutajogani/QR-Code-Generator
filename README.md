<div align="center">

# ✨ QR Code Life

**Turn any URL into a QR code in one click.**

### Turn any URL into a scannable QR code in one click.

  ![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
  ![uv](https://img.shields.io/badge/uv-managed-7C3AED?style=for-the-badge)

</div>

---

## 📖 About

QR Code Life is a small web app. Paste a URL into a clean dark page, press **Submit**, and a Python server generates a QR code that appears instantly on the page.

## 🌟 Features

- 🔗 QR code from any URL
- ⚡ Instant result, no page reload
- 🎨 Dark UI with gradients and smooth animations
- 📱 Responsive on mobile
- 🪶 Lightweight backend using only `http.server` and `qrcode`

## 🛠️ Tech Stack

| Frontend | Backend | Tooling |
| -------- | ------- | ------- |
| HTML, CSS, JavaScript | Python, `qrcode` | [uv](https://docs.astral.sh/uv/) |

## 🔌 How It Works

```
 Browser (index.html + script.js)
        │   GET /generate?url=<your-url>
        ▼
 Python server (server.py)
        │   qrcode.make(url) → PNG image
        ▼
 Browser shows the image in the <img> tag
```

## 📁 Structure

```
qr-code-generator/
├── index.html
├── style.css
├── script.js
├── server.py
└── pyproject.toml
```

## 🚀 Getting Started

**1. Install the dependency**

```bash
uv add "qrcode[pil]"
```

(or `pip install "qrcode[pil]"`)

**2. Start the server**

```bash
uv run server.py
```

The server runs on `http://localhost:8000`.

**3. Open the page**

Open `index.html` in your browser, enter a URL, and click **Submit**. 🎉

## 🔌 API

| Method | Endpoint            | Returns |
| ------ | ------------------- | ------- |
| `GET`  | `/generate?url=...` | QR code as a PNG image |

## 🧩 Troubleshooting

- **"Could not connect to the Python server"**: make sure `server.py` is running on port `8000`.
- **`ModuleNotFoundError: qrcode`**: install it with `uv add "qrcode[pil]"`.

## 👩‍💻 Author

**Ruta Jogani**
---

<div align="center">

⭐ Star this repo if you like it!

</div>