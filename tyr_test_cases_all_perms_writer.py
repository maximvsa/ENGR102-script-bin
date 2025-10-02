test_cases = open('C:/Users/maxim/engr_102/tyr_test_cases.txt', 'w')

# example test case line:
#
# sex:F age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1

error_counter = 0

possible_sex_values = ['M', 'F', 'X']
possible_age_values = [19, 20, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
possible_cho_values = [159, 160, 200, 240, 280, 300]
possible_smo_values = ['Y', 'N', 'X']
possible_hdl_values = [39, 40, 50, 60, 70]
possible_sbp_values = [119, 120, 130, 140, 160, 170]
possible_med_values = ['Y', 'N', 'X']

for sex in possible_sex_values:
    for age in possible_age_values:
        for cho in possible_cho_values:
            for smo in possible_smo_values:
                for hdl in possible_hdl_values:
                    for sbp in possible_sbp_values:
                        for med in possible_med_values:

                            try:
# Male calculations
                                if sex == 'M':

                                    if 20 <= age <= 34:
                                        out = -9
                                        
                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 4
                                        elif 200 <= cho <= 239:
                                            out += 7
                                        elif 240 <= cho <= 279:
                                            out += 9
                                        elif cho >= 280:
                                            out += 11

                                        if smo == 'Y':
                                            out += 8
                                        elif smo == 'N':
                                            out += 0
                                        
                                    elif 35 <= age <= 39:
                                        out = -4

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 4
                                        elif 200 <= cho <= 239:
                                            out += 7
                                        elif 240 <= cho <= 279:
                                            out += 9
                                        elif cho >= 280:
                                            out += 11
                                        
                                        if smo == 'Y':
                                            out += 8
                                        elif smo == 'N':
                                            out += 0

                                        
                                    elif 40 <= age <= 44:
                                        out = 0

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 3
                                        elif 200 <= cho <= 239:
                                            out += 5
                                        elif 240 <= cho <= 279:
                                            out += 6
                                        elif cho >= 280:
                                            out += 8

                                        if smo == 'Y':
                                            out += 5
                                        elif smo == 'N':
                                            out += 0

                                    elif 45 <= age <= 49:
                                        out = 3

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 3
                                        elif 200 <= cho <= 239:
                                            out += 5
                                        elif 240 <= cho <= 279:
                                            out += 6
                                        elif cho >= 280:
                                            out += 8

                                        if smo == 'Y':
                                            out += 5
                                        elif smo == 'N':
                                            out += 0

                                    elif 50 <= age <= 54:
                                        out = 6

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 2
                                        elif 200 <= cho <= 239:
                                            out += 3
                                        elif 240 <= cho <= 279:
                                            out += 4
                                        elif cho >= 280:
                                            out += 5

                                        if smo == 'Y':
                                            out += 3
                                        elif smo == 'N':
                                            out += 0

                                    elif 55 <= age <= 59:
                                        out = 8

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 2
                                        elif 200 <= cho <= 239:
                                            out += 3
                                        elif 240 <= cho <= 279:
                                            out += 4
                                        elif cho >= 280:
                                            out += 5

                                        if smo == 'Y':
                                            out += 3
                                        elif smo == 'N':
                                            out += 0

                                    elif 60 <= age <= 64:
                                        out = 10

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 1
                                        elif 200 <= cho <= 239:
                                            out += 1
                                        elif 240 <= cho <= 279:
                                            out += 2
                                        elif cho >= 280:
                                            out += 3

                                        if smo == 'Y':
                                            out += 1
                                        elif smo == 'N':
                                            out += 0

                                    elif 65 <= age <= 69:
                                        out = 11

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 1
                                        elif 200 <= cho <= 239:
                                            out += 1
                                        elif 240 <= cho <= 279:
                                            out += 2
                                        elif cho >= 280:
                                            out += 3

                                        if smo == 'Y':
                                            out += 1
                                        elif smo == 'N':
                                            out += 0

                                    elif 70 <= age <= 74:
                                        out = 12

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 0
                                        elif 200 <= cho <= 239:
                                            out += 0
                                        elif 240 <= cho <= 279:
                                            out += 1
                                        elif cho >= 280:
                                            out += 1

                                        if smo == 'Y':
                                            out += 1
                                        elif smo == 'N':
                                            out += 0

                                    elif 75 <= age <= 79:
                                        out = 13
                                    
                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 0
                                        elif 200 <= cho <= 239:
                                            out += 0
                                        elif 240 <= cho <= 279:
                                            out += 1
                                        elif cho >= 280:
                                            out += 1

                                        if smo == 'Y':
                                            out += 1
                                        elif smo == 'N':
                                            out += 0

                                    if hdl >= 60:
                                        out += -1
                                    elif 50 <= hdl <= 59:
                                        out += 0
                                    elif 40 <= hdl <= 49:
                                        out += 1
                                    elif hdl < 40:
                                        out += 2

                                    if med == 'Y':
                                        if sbp < 120:
                                            out += 0
                                        elif 120 <= sbp <= 129:
                                            out += 1
                                        elif 130 <= sbp <= 139:
                                            out += 2
                                        elif 140 <= sbp <= 159:
                                            out += 2
                                        elif sbp >= 160:
                                            out += 3

                                    elif med == 'N':
                                        if sbp < 120:
                                            out += 0
                                        elif 120 <= sbp <= 129:
                                            out += 0
                                        elif 130 <= sbp <= 139:
                                            out += 1
                                        elif 140 <= sbp <= 159:
                                            out += 1
                                        elif sbp >= 160:
                                            out += 2
                                
                                    if out < 0:
                                        out_str = '<1'
                                    elif out == 0:
                                        out_str = '1'
                                    elif out == 1:
                                        out_str = '1'
                                    elif out == 2:
                                        out_str = '1'
                                    elif out == 3:
                                        out_str = '1'
                                    elif out == 4:
                                        out_str = '1'
                                    elif out == 5:
                                        out_str = '2'
                                    elif out == 6:
                                        out_str = '2'
                                    elif out == 7:
                                        out_str = '3'
                                    elif out == 8:
                                        out_str = '4'
                                    elif out == 9:
                                        out_str = '5'
                                    elif out == 10:
                                        out_str = '6'
                                    elif out == 11:
                                        out_str = '8'
                                    elif out == 12:
                                        out_str = '10'
                                    elif out == 13:
                                        out_str = '12'
                                    elif out == 14:
                                        out_str = '16'
                                    elif out == 15:
                                        out_str = '20'
                                    elif out == 16:
                                        out_str = '25'
                                    elif out >= 17:
                                        out_str = '>=30'
# Female calculations
                                elif sex == 'F':
                                    
                                    if 20 <= age <= 34:
                                        out = -7

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 4
                                        elif 200 <= cho <= 239:
                                            out += 8
                                        elif 240 <= cho <= 279:
                                            out += 11
                                        elif cho >= 280:
                                            out += 13

                                        if smo == 'Y':
                                            out += 9
                                        elif smo == 'N':
                                            out += 0
                                        
                                    elif 35 <= age <= 39:
                                        out = -3

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 4
                                        elif 200 <= cho <= 239:
                                            out += 8
                                        elif 240 <= cho <= 279:
                                            out += 11
                                        elif cho >= 280:
                                            out += 13

                                        if smo == 'Y':
                                            out += 9
                                        elif smo == 'N':
                                            out += 0

                                    elif 40 <= age <= 44:
                                        out = 0

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 3
                                        elif 200 <= cho <= 239:
                                            out += 6
                                        elif 240 <= cho <= 279:
                                            out += 8
                                        elif cho >= 280:
                                            out += 10

                                        if smo == 'Y':
                                            out += 7
                                        elif smo == 'N':
                                            out += 0

                                    elif 45 <= age <= 49:
                                        out = 3

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 3
                                        elif 200 <= cho <= 239:
                                            out += 6
                                        elif 240 <= cho <= 279:
                                            out += 8
                                        elif cho >= 280:
                                            out += 10

                                        if smo == 'Y':
                                            out += 7
                                        elif smo == 'N':
                                            out += 0

                                    elif 50 <= age <= 54:
                                        out = 6

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 2
                                        elif 200 <= cho <= 239:
                                            out += 4
                                        elif 240 <= cho <= 279:
                                            out += 5
                                        elif cho >= 280:
                                            out += 7

                                        if smo == 'Y':
                                            out += 4
                                        elif smo == 'N':
                                            out += 0

                                    elif 55 <= age <= 59:
                                        out = 8

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 2
                                        elif 200 <= cho <= 239:
                                            out += 4
                                        elif 240 <= cho <= 279:
                                            out += 5
                                        elif cho >= 280:
                                            out += 7

                                        if smo == 'Y':
                                            out += 4
                                        elif smo == 'N':
                                            out += 0

                                    elif 60 <= age <= 64:
                                        out = 10

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 1
                                        elif 200 <= cho <= 239:
                                            out += 2
                                        elif 240 <= cho <= 279:
                                            out += 3
                                        elif cho >= 280:
                                            out += 4

                                        if smo == 'Y':
                                            out += 2
                                        elif smo == 'N':
                                            out += 0

                                    elif 65 <= age <= 69:
                                        out = 12

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 1
                                        elif 200 <= cho <= 239:
                                            out += 2
                                        elif 240 <= cho <= 279:
                                            out += 3
                                        elif cho >= 280:
                                            out += 4

                                        if smo == 'Y':
                                            out += 2
                                        elif smo == 'N':
                                            out += 0

                                    elif 70 <= age <= 74:
                                        out = 14

                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 1
                                        elif 200 <= cho <= 239:
                                            out += 1
                                        elif 240 <= cho <= 279:
                                            out += 2
                                        elif cho >= 280:
                                            out += 2

                                        if smo == 'Y':
                                            out += 1
                                        elif smo == 'N':
                                            out += 0

                                    elif 75 <= age <= 79:
                                        out = 16
                                    
                                        if cho < 160:
                                            out += 0
                                        elif 160 <= cho <= 199:
                                            out += 1
                                        elif 200 <= cho <= 239:
                                            out += 1
                                        elif 240 <= cho <= 279:
                                            out += 2
                                        elif cho >= 280:
                                            out += 2

                                        if smo == 'Y':
                                            out += 1
                                        elif smo == 'N':
                                            out += 0

                                    if hdl >= 60:
                                        out += -1
                                    elif 50 <= hdl <= 59:
                                        out += 0
                                    elif 40 <= hdl <= 49:
                                        out += 1
                                    elif hdl < 40:
                                        out += 2

                                    if med == 'Y':
                                        if sbp < 120:
                                            out += 0
                                        elif 120 <= sbp <= 129:
                                            out += 3
                                        elif 130 <= sbp <= 139:
                                            out += 4
                                        elif 140 <= sbp <= 159:
                                            out += 5
                                        elif sbp >= 160:
                                            out += 6
                                            
                                    elif med == 'N':
                                        if sbp < 120:
                                            out += 0
                                        elif 120 <= sbp <= 129:
                                            out += 1
                                        elif 130 <= sbp <= 139:
                                            out += 2
                                        elif 140 <= sbp <= 159:
                                            out += 3
                                        elif sbp >= 160:
                                            out += 4

                                    if out < 9:
                                        out_str = '<1'
                                    elif out == 9:
                                        out_str = '1'
                                    elif out == 10:
                                        out_str = '1'
                                    elif out == 11:
                                        out_str = '1'
                                    elif out == 12:
                                        out_str = '1'
                                    elif out == 13:
                                        out_str = '2'
                                    elif out == 14:
                                        out_str = '2'
                                    elif out == 15:
                                        out_str = '3'
                                    elif out == 16:
                                        out_str = '4'
                                    elif out == 17:
                                        out_str = '5'
                                    elif out == 18:
                                        out_str = '6'
                                    elif out == 19:
                                        out_str = '8'
                                    elif out == 20:
                                        out_str = '11'
                                    elif out == 21:
                                        out_str = '14'
                                    elif out == 22:
                                        out_str = '17'
                                    elif out == 23:
                                        out_str = '22'
                                    elif out == 24:
                                        out_str = '27'
                                    elif out >= 25:
                                        out_str = '>=30'
                        
                                test_case_line = f'sex:{sex} age:{age} cho:{cho} smo:{smo} hdl:{hdl} sbp:{sbp} med:{med} out:{out_str}'
                                test_cases.write(f'{test_case_line}\n')

                            except Exception:

                                print(f'Error with test case: sex:{sex} age:{age} cho:{cho} smo:{smo} hdl:{hdl} sbp:{sbp} med:{med}')
                                error_counter += 1
                                print(f'Error count: {error_counter}')
                                