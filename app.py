from flask import Flask, render_template
from supabase import create_client

app = Flask(__name__)

SUPABASE_URL = "https://pttflbhytpuktdzppzyq.supabase.co"
SUPABASE_KEY = "sb_publishable_ThJfbUmkbQ0bvGWL2so_QQ_n35QH096"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

@app.route("/")

def home():

    data = (
        supabase.table("nike_products")
        .select("*")
        .limit(100)
        .execute()
    )

    products = data.data

    return render_template(
        "index.html",
        products=products
    )

if __name__ == "__main__":
    app.run(debug=True)