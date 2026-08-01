class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_card = []

        for i in range(len(operations)):
            print(score_card)
            
            if operations[i] == "+":
                new_score = score_card[-1] + score_card[-2]
                score_card.append(new_score)
            elif operations[i] == "C":
                score_card.pop()
            elif operations[i] == "D":
                new_score = 2*score_card[-1]
                score_card.append(new_score)
            else:
                score_card.append(int(operations[i]))
        
        return sum(score_card)