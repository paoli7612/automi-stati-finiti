import json
from AFD import AutomaDeterministico

def load_automaton_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    name = data['name']
    alphabet = set(data['alphabet'])
    states = set(data['states'])
    start_state = data['start_state']
    final_states = set(data['final_states'])
    transitions = dict()

    for state, trans in data['transitions'].items():
        for symbol, target_state in trans.items():
            transitions[(state, symbol)] = target_state

    AutomaDeterministico(
        name=name,
        alphabet=alphabet,
        states=states,
        start_state=start_state,
        final_states=final_states,
        transitions=transitions
    )

if __name__ == '__main__':
    load_automaton_from_json('input/1.json')
    load_automaton_from_json('input/2.json')

