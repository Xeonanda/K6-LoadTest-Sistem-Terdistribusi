# Server yang menangani pemanggilan API

from flask import Flask, send_file, abort, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <title>Simple File API</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100 text-gray-800">
        <div class="min-h-screen flex items-center justify-center">
            <div class="bg-white shadow-md rounded-lg p-8 max-w-lg text-center">
                <h1 class="text-3xl font-semibold text-blue-600 mb-4">Hello!</h1>
                <p class="text-lg mb-6">
                    Ini adalah API sederhana yang menyediakan file teks berukuran:
                </p>
                <ul class="list-disc list-inside text-left mb-6">
                    <li><code>/api/10</code> - file 10KB</li>
                    <li><code>/api/100</code> - file 100KB</li>
                    <li><code>/api/1000</code> - file 1MB</li>
                </ul>
                <p class="text-sm text-gray-600">
                    File disediakan dari folder lokal dan bisa digunakan untuk keperluan load testing.
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/api/<int:size_kb>', methods=['GET'])
def serve_file(size_kb):
    file_map = {
        10: 'files/10kb.txt',
        100: 'files/100kb.txt',
        1000: 'files/1000kb.txt',
    }

    file_path = file_map.get(size_kb)
    if file_path:
        return send_file(file_path, mimetype='text/plain',as_attachment=True)
    else:
        abort(404, description="File size not supported.")

@app.errorhandler(404)
def page_not_found(e):
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <title>404 - Tidak Ditemukan</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100 text-gray-800">
        <div class="min-h-screen flex items-center justify-center">
            <div class="text-center">
                <h1 class="text-6xl font-bold text-blue-600 mb-4">404</h1>
                <p class="text-xl mb-2">Halaman tidak ditemukan.</p>
                <a href="/" class="text-blue-500 hover:underline">Kembali ke beranda</a>
            </div>
        </div>
    </body>
    </html>
    """), 404

if __name__ == '__main__':
    app.run(debug=True)
