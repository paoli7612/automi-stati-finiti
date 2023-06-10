import graphviz

class AutomaDeterministico:
    def __init__(self, name, alphabet, states, start_state, final_states, transitions):
        self.alphabet = alphabet
        self.states = states
        self.start_state = start_state
        self.final_states = final_states
        self.transitions = transitions

        dot = self.to_dot()
        dot.render('out/'+name, format='png')

    def accept(self, input, debug=False):
        state = self.start_state
        for i in input:
            if debug:
                print("Input:", i, "Stato corrente:", state, end=" ")
            if (state, i) in self.transitions:
                state = self.transitions[(state, i)]
            else:
                if debug: print("input non accettato")
                return False
            if debug: print("->", state)
        return state in self.final_states

    def to_dot(self):
        dot = graphviz.Digraph()

        # Aggiungi gli stati
        for state in self.states:
            if state == self.start_state:
                dot.node(state, shape='doublecircle', color='green')  # Lo stato iniziale è evidenziato in verde
            elif state in self.final_states:
                dot.node(state, shape='doublecircle')
            else:
                dot.node(state, shape='circle')

        # Aggiungi le transizioni
        for (state, input), next_state in self.transitions.items():
            dot.edge(state, next_state, label=input)

        return dot