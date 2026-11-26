# GA Assignment

Student name: ____________________

Student ID: ____________________

Course / section: ____________________

Submission date: ____________________

## Final submission files

- `Genetic_Algorithm_Assignment.pdf`
- `genetic_algorithm_route.py`
- `evidence/console_output.txt`
- `evidence/best_route.png`

## PDF contents

The PDF should contain:

1. Student cover details.
2. Part A - Understanding the Problem.
3. Part B - Design the Genetic Algorithm.
4. Part D - Evaluate Your Result.
5. The best route and total distance.
6. A screenshot or copied console output in the PDF.

Do not use the Lab 8 medical-insurance dataset. Use only the fictional
delivery-distance matrix provided in the assignment.

## Python source

The Python source should:

- Represent a route as a permutation of `B`, `C`, `D`, `E`, `F`, and `G`.
- Start and finish every route at `A`.
- Use an initial population containing valid routes.
- Calculate the total route distance, including the return to `A`.
- Use tournament or another stated selection method.
- Use route-preserving crossover.
- Apply a small mutation that still preserves a valid route.
- Copy elite routes unchanged.
- Use at least 50 generations.
- Use a fixed random seed.
- Print the best route and total distance.

## Submission checklist

- [ ] PDF exported and saved as `Genetic_Algorithm_Assignment.pdf`
- [ ] Python source saved as `genetic_algorithm_route.py`
- [ ] Console output copied to `evidence/console_output.txt`
- [ ] Screenshot saved to `evidence/best_route.png`
- [ ] PDF and source added to this repository folder
- [ ] Evidence files added to `evidence/`
- [ ] Fictional distance matrix used rather than the insurance data
