import sys
import json
from client import PlonkPermutationArgument

plonk = PlonkPermutationArgument()

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "plonk_permutation_check",
                        "description": "Compute Plonk grand product copy constraint permutation argument",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "wire_values": {"type": "array", "items": {"type": "integer"}},
                                "sigma_perm": {"type": "array", "items": {"type": "integer"}}
                            },
                            "required": ["wire_values", "sigma_perm"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "plonk_permutation_check":
            z = plonk.compute_grand_product(args["wire_values"], args["sigma_perm"])
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"grand_product": z, "valid": z == 1})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
