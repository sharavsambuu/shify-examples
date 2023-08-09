# Trading algo implementation

def initialize(ctx):
    print(f"algo init {ctx}")

def handle_data(ctx, state):
    print(f"context : {ctx}, state : {state}")
