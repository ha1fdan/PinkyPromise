from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
import uuid
from datetime import datetime
import os

app = Flask(__name__)

# File to store promises
PROMISES_FILE = 'promises.json'
if not os.path.exists(PROMISES_FILE):
    with open(PROMISES_FILE, 'w') as f:
        json.dump({}, f)

def save_promise(promise):
    """Save promise to JSON file"""
    try:
        with open(PROMISES_FILE, 'r') as f:
            promises = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        promises = {}
    
    promises[promise['id']] = promise
    
    with open(PROMISES_FILE, 'w') as f:
        json.dump(promises, f, indent=4)

def get_promise(promise_id):
    """Retrieve a specific promise"""
    try:
        with open(PROMISES_FILE, 'r') as f:
            promises = json.load(f)
        return promises.get(promise_id)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

@app.route('/', methods=['GET', 'POST'])
def create_promise():
    """Create a new pinky promise"""
    if request.method == 'POST':
        # Generate a unique ID for the promise
        promise_id = str(uuid.uuid4())[:8]
        
        # Create promise object
        promise = {
            'id': promise_id,
            'description': request.form['description'],
            'due_date': request.form['due_date'],
            'creator': request.form['creator'],
            'signatures': [],
            'created_at': datetime.now().isoformat()
        }
        
        # Save the promise
        save_promise(promise)
        
        # Redirect to the promise page
        return redirect(url_for('view_promise', promise_id=promise_id))
    
    return render_template('create_promise.html')

@app.route('/promise/<promise_id>', methods=['GET', 'POST'])
def view_promise(promise_id):
    """View and sign a promise"""
    promise = get_promise(promise_id)
    
    if not promise:
        return render_template('404.html'), 404
    
    if datetime.strptime(promise['due_date'], '%Y-%m-%d') < datetime.now():
        signing_disabled = True
    else:
        signing_disabled = False
    
    if request.method == 'POST' and not signing_disabled:
        # Add a signature
        signature = {
            'name': request.form['name'],
            'signed_at': datetime.now().isoformat()
        }
        
        # Prevent duplicate signatures
        if not any(sig['name'] == signature['name'] for sig in promise['signatures']):
            promise['signatures'].append(signature)
            save_promise(promise)
        
        return redirect(url_for('view_promise', promise_id=promise_id))
    
    return render_template('view_promise.html', promise=promise, signing_disabled=signing_disabled)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)