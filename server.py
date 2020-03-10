from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def main():
  return "HooHacks + MLC@UVA Demo"

if __name__ == '__main__':
  app.run(debug=True)