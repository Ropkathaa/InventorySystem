from flask import Flask, request, jsonify
from db.mongo_client import collection

from db.redis_client import r
from db.neo4j_client import driver
app = Flask(__name__)


@app.route('/')
def home():
    return "Inventory System Running 🚀"



# VIEW ALL PRODUCTS
@app.route('/get_products', methods=['GET'])
def get_products():
    products = list(collection.find({}, {"_id": 0}))
    return jsonify(products)  # GET PRODUCT BY ID


@app.route('/get_product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = collection.find_one({"id": product_id}, {"_id": 0})

    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404
# UPDATE PRODUCT
@app.route('/update_product/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json

    result = collection.update_one(
        {"id": product_id},
        {"$set": data}
    )

    if result.modified_count > 0:
        return jsonify({"message": "Product updated"})
    else:
        return jsonify({"error": "Product not found or no change"}), 404
# DELETE PRODUCT
@app.route('/delete_product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    result = collection.delete_one({"id": product_id})

    if result.deleted_count > 0:
        return jsonify({"message": "Product deleted"})
    else:
        return jsonify({"error": "Product not found"}), 404


@app.route('/ratelimit')
def rate_limit():
    ip = request.remote_addr

    count = r.get(ip)

    if count and int(count) >= 5:
        return jsonify({"error": "Rate limit exceeded"}), 429
    else:
        r.incr(ip)
        r.expire(ip, 60)
        return jsonify({"message": "Request allowed"})
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json

    # Save in MongoDB
    collection.insert_one(data)

    # Save in Neo4j
    with driver.session() as session:
        session.run(
            """
            MERGE (p:Product {id: $pid, name: $pname})
            MERGE (m:Manufacturer {name: $mname})
            MERGE (p)-[:MANUFACTURED_BY]->(m)
            """,
            pid=data.get("id"),
            pname=data.get("name"),
            mname=data.get("manufacturer", "Unknown")
        )

    return jsonify({"message": "Product added in MongoDB + Neo4j"})
if __name__ == '__main__':
    app.run(debug=True)
