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

if __name__ == '__main__':
    # Automa AFD1  accetta  ( 01*0 ) -> uno 0, zero o più 1, uno 0
    AFD1 = AutomaDeterministico(
        name='AFD1',
        alphabet = {'0', '1'},      # alfabeto = 0 1
        states = {'A', 'B', 'C'},   # stati = A B C
        start_state = 'A',          # stato iniziale = A
        final_states = {'C'},       # stati finali = C
        transitions = {             # transizioni: 
            ('A', '0'): 'B',            # Dallo stato A con input 0 transita in B
            ('B', '0'): 'C',            # Dallo stato B con input 0 transita in C
            ('B', '1'): 'B'             # Dallo stato B con input 1 rimani in B
        }
    )

    # esempio
    AFD2 = AutomaDeterministico(
        name='AFD2',
        alphabet = {'0', '1', '2'},             # alfabeto = 0 1 2
        states = {'1', '2', '3', '4', '5'},     # stati = 1 2 3 4 5
        start_state = '1',                      # stato iniziale = 1
        final_states = {'4', '5'},              # stati finali = C
        transitions = {                         # transizioni: 
            ('1', '0'): '3',
            ('1', '1'): '5',
            ('2', '0'): '5',
            ('2', '1'): '4',
            ('3', '0'): '4',
            ('3', '1'): '2',
            ('4', '0'): '5',
            ('4', '1'): '5',
            ('5', '0'): '3',
        }
    )
    result = ['Rifiutato', 'Accettato']
    print(result[AFD2.accept('0000010110', True)])

    AutomaDeterministico(
        name='soloCopieDiNumeri',
        alphabet = {'0', '1'},                  # alfabeto = 0 1 2
        states = {'0', '1', '2'},               # stati = 1 2 3 4 5
        start_state = '0',                      # stato iniziale = 1
        final_states = {'0'},                   # stati finali = C
        transitions = {                         # transizioni: 
            ('0', '0'): '1',        # se entra uno 0
            ('0', '1'): '2',            # sentra un 1
            ('1', '0'): '0',        # ..solo se entra un altro 0 torniamo allo stato iniziale/finale
            ('2', '1'): '0'             # ..solo se entra un altro 1 torniamo allo stato iniziale/finale
        }
    )
