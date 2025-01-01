async function calculateSubnets() {
    const vpcCidr = document.getElementById("vpc-cidr").value;
    const numSubnets = document.getElementById("num-subnets").value;

    const response = await fetch('http://localhost:5000/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ vpc_cidr: vpcCidr, num_subnets: numSubnets })
    });

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = ""; // Clear previous results

    if (response.ok) {
        const result = await response.json();
        result.forEach(subnet => {
            const subnetDiv = document.createElement("div");
            subnetDiv.innerHTML = `Subnet: ${subnet.subnet}, IP Range: ${subnet.ip_range}`;
            resultDiv.appendChild(subnetDiv);
        });
    } else {
        const error = await response.json();
        resultDiv.innerHTML = `Error: ${error.error}`;
    }
}
