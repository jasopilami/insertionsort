def insertion_sort(arr):
  # elemente muessen verglichen werden deswegen bei 0 anfangen kein sinn
  # wir sortieren nach links ein
  for index in range(1, len(arr)):
    # das element welches wir einsortieren wollen
    number_to_sort = arr[index]
    # der index vom vorherigen element
    sort_into_index = index - 1
 
    # wir suchen den richtigen index im sortierten bereich fuer das element
    while number_to_sort < arr[sort_into_index] and sort_into_index >= 0:
      # solange a < b shiften wir das array nach links
      arr[sort_into_index + 1] = arr[sort_into_index]
      sort_into_index -= 1
 
    # nach dem shiften koennen wir das element an die richtige stelle inserten
    arr[sort_into_index + 1] = number_to_sort
 
input = [5, 2, 4, 6, 1, 3]
 
insertion_sort(input)
 
print(input)