# 🎙️ Podcast2Zim Scraper Prototype

### GSoC 2026 | Organization: Kiwix / OpenZIM

This repository contains a functional end-to-end prototype for the **podcast2zim** scraper. The project automates the extraction of podcast episodes from RSS feeds, downloads the associated media, and packages them into the high-compression `.zim` format for offline consumption via the Kiwix reader.

---

## 🚀 Key Features

* **RSS Ingestion:** Fully automated parsing of XML/RSS feeds using the `feedparser` library to extract titles, descriptions, and high-quality media enclosures.
* **Media Management:** Robust downloading of audio assets (MP3/AAC) with error handling and local directory management.
* **ZIM Packaging:** Seamless integration with the latest `libzim` (3.8.0) standards to create indexed, searchable offline archives.
* **API Resilience:** Implements a custom `Item` class and `FileProvider` architecture to resolve recent breaking changes in the Python libzim bindings.

---

## 🛠️ Technical Architecture

The scraper operates on a modular pipeline designed for scalability:

1.  **Parser Layer:** Connects to remote podcast feeds and maps XML metadata to internal Python objects.
2.  **Asset Layer:** Handles HTTP requests to fetch binary data and stores them in a temporary structure.
3.  **Zimification Layer:** Uses a multi-threaded writer to package HTML headers, metadata, and audio content into a single, portable ZIM file.



---

## 📦 Installation & Usage

### 1. Prerequisites
Ensure you have Python 3.10 or higher. Install the necessary dependencies via the terminal:

```bash
pip install feedparser requests libzim
```
### 2. Scraping Content
Run the scraper to fetch episodes from the target RSS feed:

```Bash
python scraper.py
```
### 3. Creating the ZIM Archive
Once your downloads/ folder contains the MP3 files, run the packager:

```Bash
python make_zim.py
```
The final output, my_podcast.zim, will be generated in your root directory.


---

### 🔧 Technical Challenges & Solutions

> **The Problem:** > During development with `libzim 3.8.0`, I encountered a major API shift where the `add_item()` method stopped accepting standard positional arguments (path, mimetype, data), throwing a `TypeError: add_item() takes exactly 1 positional argument (3 given)`.

> **The Discovery:** > After analyzing the `libzim` source and tracing the error back to the Python-C++ wrapper layer, I realized the base `Item` class had become abstract, and the writer now requires a single, structured object to maintain memory safety and metadata integrity.

> **The Solution:** > I successfully implemented a custom subclass of `libzim.writer.Item` and utilized `libzim.writer.FileProvider`. By overriding the `get_path()`, `get_mimetype()`, and `get_contentprovider()` methods, I created a robust bridge between the local filesystem and the ZIM archive. This solution aligns with the architecture used in professional OpenZIM scrapers like `youtube2zim`.




---



## 👨‍💻 About the Author

| **Attribute** | **Details** |
| :--- | :--- |
| **Name** | Hari Om Singh |
| **Education** | B.Tech in Computer Science & Engineering |
| **Institution** | B.I.T. Sindri (Batch of 2027) |
| **Technical Focus** | AI Engineering, OpenZIM Infrastructure, Backend Systems |
| **Location** | Daltonganj, Jharkhand, India |

### 🌟 Technical Interests
* **Open Source:** Passionate about making educational content accessible in low-connectivity areas via the Kiwix ecosystem.
* **Development:** Proficient in Python and C++, with a strong foundation in Data Structures and Algorithms (DSA).
* **AI/ML:** Experienced in building OCR pipelines and automated tool managers.

### 🔗 Connect with Me
* **GitHub:** [@hari-om65](https://github.com/hari-om65)
* **LinkedIn:** [www.linkedin.com/in/hariom765]
