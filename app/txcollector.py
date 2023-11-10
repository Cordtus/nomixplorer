import websocket
import base64
import json
import threading

def on_message(ws, message):
    try:
        # Parse the JSON message
        json_message = json.loads(message)
        
        # Check if the 'result' and 'data' fields are in the message
        if 'result' in json_message and 'data' in json_message['result']:
            data = json_message['result']['data']
            if 'value' in data and 'TxResult' in data['value'] and 'tx' in data['value']['TxResult']:
                # Decode the base64-encoded transaction
                encoded_tx = data['value']['TxResult']['tx']
                decoded_tx = base64.b64decode(encoded_tx)
                
                # Convert the binary data to a JSON string (assuming it's JSON-encoded)
                try:
                    decoded_json_str = decoded_tx.decode('utf-8')
                    decoded_json_obj = json.loads(decoded_json_str)
                    print(json.dumps(decoded_json_obj, indent=2))  # Pretty print the JSON object
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from transaction: {e}")
                except UnicodeDecodeError as e:
                    print(f"Error decoding UTF-8 from transaction: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON message: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"WebSocket closed with status code: {close_status_code}, close message: {close_msg}")

def on_open(ws):
    def run(*args):
        # Send the subscription message to the WebSocket server
        subscribe_message = {
            "jsonrpc": "2.0",
            "method": "subscribe",
            "id": "sub-0",
            "params": {
                "query": "tm.event = 'Tx'"
            }
        }
        ws.send(json.dumps(subscribe_message))
        print("Subscribed to transactions...")
    threading.Thread(target=run).start()

# Enable websocket logging
websocket.enableTrace(True)

# Create a websocket app
ws_app = websocket.WebSocketApp("wss://rpc.nomic.basementnodes.ca/websocket",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

# Run the websocket app
ws_app.run_forever()
