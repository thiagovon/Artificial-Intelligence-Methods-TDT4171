import numpy as np

def forward_filtering(evidence_sequence):
    T = np.array([[0.7, 0.3], 
                  [0.3, 0.7]])
    T_transposta = T.T
    O_true = np.diag([0.9, 0.2])
    O_false = np.diag([0.1, 0.8])
    
    f_vector = np.array([0.5, 0.5])
    results = []
    
    print(f"{'Day':<5} | {'Observation':<12} | {'P(Rain)':<10} | {'P(Sun)':<10}")
    print("-" * 45)

    for i, has_umbrella in enumerate(evidence_sequence, 1):
        if has_umbrella:
            O_t = O_true
            obs_str = "True"
        else:
            O_t = O_false
            obs_str = "False"
        
        predicao = np.dot(T_transposta, f_vector)

        f_nao_normalizado = np.dot(O_t, predicao)
        

        alpha = 1.0 / np.sum(f_nao_normalizado)
        f_vector = alpha * f_nao_normalizado
        
        results.append(f_vector)
        print(f"{i:<5} | {obs_str:<12} | {f_vector[0]:.4f}     | {f_vector[1]:.4f}")

    return results

if __name__ == "__main__":
    print("\n=== Verification (Days 1-2) ===")
    evidence_verify = [True, True]
    final_verify = forward_filtering(evidence_verify)[-1]
    
    print(f"\nExpected P(Rain|e1:2) aprox 0.883.")
    print(f"Calculated P(Rain|e1:2) = {final_verify[0]:.4f}")
    
    print("\n=== Final Task (Days 1-5) ===")
    evidence_task = [True, True, False, True, True]
    forward_filtering(evidence_task)