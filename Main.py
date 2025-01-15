import VectorGenerationAndRating as VGR
import TorneoBinario as TB
import pandas as pd

if __name__ == "__main__":
   pd.set_option('display.max_rows', None)
   pd.set_option('display.max_columns', None)
   pd.set_option('display.width', 1000)
   pd.set_option('display.colheader_justify', 'center')
   solutions = VGR.CreateSolutionsVector(100, 100)
   scores = [VGR.CalculateVO(solution) for solution in solutions]
   parents = TB.GetNextGenerationParents(solutions, scores, 50)
   print(pd.DataFrame(parents))
