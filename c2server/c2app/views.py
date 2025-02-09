from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

EMPIRE_API_URL = "http://127.0.0.1:1337/api"
EMPIRE_USERNAME = "admin"
EMPIRE_PASSWORD = "empire123"

def get_empire_token():
    """Authenticate with Empire API and return a session token."""
    response = requests.post(f"{EMPIRE_API_URL}/admin/login", json={
        "username": EMPIRE_USERNAME,
        "password": EMPIRE_PASSWORD
    })
    return response.json().get("token")

MSF_RPC_URL = "http://127.0.0.1:55553/api/v1"
USERNAME = "msf"
PASSWORD = "yourpassword"

def get_msf_token():
    """Authenticate with Metasploit and get a session token."""
    response = requests.post(f"{MSF_RPC_URL}/auth/login", json={
        "username": USERNAME,
        "password": PASSWORD
    })
    return response.json().get("token")

@api_view(['GET'])
def list_empire_agents(request):
    """List active Empire agents."""
    agents = get_empire_agents()
    return Response(agents)

@api_view(['POST'])
def execute_empire_command(request):
    """Execute a command on a given Empire agent."""
    agent_name = request.data.get("agent_name")
    command = request.data.get("command")
    result = run_empire_command(agent_name, command)
    return Response(result)

def get_active_sessions():
    """Retrieve active Meterpreter sessions."""
    token = get_msf_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(f"{MSF_RPC_URL}/sessions/list", headers=headers)
    return response.json()

def run_command(session_id, command):
    """Run a shell command on a Meterpreter session."""
    token = get_msf_token()
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "session_id": session_id,
        "command": command
    }
    response = requests.post(f"{MSF_RPC_URL}/sessions/{session_id}/shell_write", json=payload, headers=headers)
    return response.json()

@api_view(['GET'])
def list_sessions(request):
    """List all active Meterpreter sessions."""
    sessions = get_active_sessions()
    return Response(sessions)

@api_view(['POST'])
def execute_command(request):
    """Execute a command on a given session."""
    session_id = request.data.get("session_id")
    command = request.data.get("command")
    result = run_command(session_id, command)
    return Response(result)
