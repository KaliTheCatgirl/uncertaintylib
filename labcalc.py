from uncertaintylib import *

# calculations used in lab
if __name__ == "__main__":
    # trial 1
    salt_sample_mass = scinum(0.1001, 0.0001, 4) # g
    beaker_paper_mass = scinum(26.7684, 0.0001, 6) # g
    beaker_paper_precipitate_mass = scinum(26.9355, 0.0001, 6) # g
    precipitate_mass = beaker_paper_precipitate_mass - beaker_paper_mass
    print(f"Mass of precipitate: {precipitate_mass}g")
    agcl_molar_mass = 143.32 # g/mol
    cl_molar_mass = 35.45 # g/mol
    moles_agcl = precipitate_mass / agcl_molar_mass # mol
    cl_mass = moles_agcl * cl_molar_mass # g
    cl_content_1 = cl_mass / salt_sample_mass
    print(f"Mass of chlorine: {cl_mass}g")
    print(f"Chlorine mass percentage: {cl_content_1 * 100}%")
    
    print()
    
    # trial 2
    salt_sample_mass = scinum(0.1027, 0.0001, 4) # g
    beaker_paper_mass = scinum(28.8843, 0.0001, 6) # g
    beaker_paper_precipitate_mass = scinum(29.0981, 0.0001, 6) # g
    precipitate_mass = beaker_paper_precipitate_mass - beaker_paper_mass
    print(f"Mass of precipitate: {precipitate_mass}g")
    agcl_molar_mass = 143.32 # g/mol
    cl_molar_mass = 35.45 # g/mol
    moles_agcl = precipitate_mass / agcl_molar_mass # mol
    cl_mass = moles_agcl * cl_molar_mass # g
    cl_content_2 = cl_mass / salt_sample_mass
    print(f"Mass of chlorine: {cl_mass}g")
    print(f"Chlorine mass percentage: {cl_content_2 * 100}%")

    print()

    avg_content = (cl_content_1 + cl_content_2) / 2
    expected = 54.1
    print(f"Average chlorine mass percentage: {avg_content * 100}%")
    print(f"Relative error: {((avg_content * 100 - expected) / expected).abs() * 100}%")
    print(f"Relative spread: {(cl_content_2 - cl_content_1) / avg_content * 1000}ppt")
