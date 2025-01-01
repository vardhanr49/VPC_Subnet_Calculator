from flask import Flask, request, jsonify
import ipaddress

app = Flask(__name__)

@app.route('/')
def home():
    return "VPC Subnet Calculator Backend is Running"

@app.route('/calculate', methods=['POST'])
def calculate_subnets():
    data = request.json
    vpc_cidr = data.get('vpc_cidr')
    num_subnets = int(data.get('num_subnets'))

    try:
        # Calculate subnets
        vpc = ipaddress.IPv4Network(vpc_cidr, strict=False)
        new_prefix = vpc.prefixlen + (num_subnets - 1).bit_length()

        if new_prefix > 32:
            return jsonify({"error": f"Cannot divide {vpc_cidr} into {num_subnets} subnets"}), 400

        subnets = list(vpc.subnets(new_prefix=new_prefix))
        result = [{"subnet": str(subnet), "ip_range": f"{subnet[0]} - {subnet[-1]}"} for subnet in subnets]
        return jsonify(result)

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
