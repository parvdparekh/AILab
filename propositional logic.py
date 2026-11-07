import itertools

def evaluate(expr, model):
    """Evaluates propositional logic expressions under a model."""
    if isinstance(expr, str):
        return model[expr]
    
    op = expr[0]
    if op == 'NOT':
        return not evaluate(expr[1], model)
    elif op == 'AND':
        return evaluate(expr[1], model) and evaluate(expr[2], model)
    elif op == 'OR':
        return evaluate(expr[1], model) or evaluate(expr[2], model)
    elif op == 'IMPLIES':
        return (not evaluate(expr[1], model)) or evaluate(expr[2], model)

def check_entailment_size_2(symbols, sentences, queries):
    """Generates truth table for size-2 variables and checks multiple queries."""
    query_names = list(queries.keys())
    
    # Table Header
    header = f"{' | '.join(symbols)} | S1 | S2 | **KB** | " + " | ".join(query_names)
    print("=" * len(header))
    print(header)
    print("=" * len(header))
    
    entails = {q: True for q in queries}
    
    # Iterate through all 2^2 = 4 truth assignments
    for values in itertools.product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        
        # Evaluate KB sentences
        s1 = evaluate(sentences[0], model)
        s2 = evaluate(sentences[1], model)
        
        kb_val = s1 and s2
        
        # Evaluate queries for this row
        q_vals = {}
        for q_name, q_expr in queries.items():
            val = evaluate(q_expr, model)
            q_vals[q_name] = val
            
            # Entailment rule: KB=True implies Query=True
            if kb_val and not val:
                entails[q_name] = False
                
        # Format truth table output
        sym_str = " | ".join(" T " if model[s] else " F " for s in symbols)
        kb_str = " T  " if kb_val else " F  "
        s_str = f"{'T' if s1 else 'F'}  | {'T' if s2 else 'F'}"
        q_str = " | ".join(f"   {'T' if q_vals[q] else 'F'}   " for q in query_names)
        
        print(f"{sym_str} | {s_str} |  {kb_str} | {q_str}")

    print("=" * len(header))
    
    # Summary Output
    print("\n=== Entailment Results ===")
    for q_name, result in entails.items():
        symbol = "⊨" if result else "⊭"
        status = "ENTAILED" if result else "NOT ENTAILED"
        print(f"• KB {symbol} ({q_name}) : {status}")

# --- Setup for 2 Variables ---
symbols = ['P', 'Q']

# KB: (P -> Q) AND P
kb_sentences = [
    ('IMPLIES', 'P', 'Q'),  # S1: P -> Q
    'P'                     # S2: P
]

# Two Queries to test
queries = {
    "α1: Q": 'Q',
    "α2: ~P": ('NOT', 'P')
}

# Run
check_entailment_size_2(symbols, kb_sentences, queries)