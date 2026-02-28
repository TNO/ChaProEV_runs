import os
import shutil

import pandas as pd
from ChaProEV import ChaProEV
from ETS_CookBook import ETS_CookBook as cook


def copy_select_files(case_name: str) -> None:
    desired_output_elements: list[str] = [
        # 'profile_fleet',
        # 'weekly_consumption_table_fleet',
        'profile',
        'weekly_consumption_table',
    ]
    select_output_folder: str = f'select_output/{case_name}/'
    cook.check_if_folder_exists(select_output_folder)
    for output_file in os.listdir(f'output/{case_name}'):
        if any(
            output_file.split('.')[0].endswith(desired_output_element)
            for desired_output_element in desired_output_elements
        ):
            # if any(
            #     desired_output_element in output_file
            #     for desired_output_element in desired_output_elements
            # ):
            if output_file.endswith('.csv'):
                if 'XX' not in output_file:
                    if 'driveway' not in output_file:
                        if 'street' not in output_file:
                            shutil.copy(
                                f'output/{case_name}/{output_file}',
                                select_output_folder,
                            )


def rename_files_with_country_codes(case_name: str) -> None:
    select_output_folder: str = f'select_output/{case_name}/'
    country_codes: pd.DataFrame = pd.read_csv('country_codes.csv').set_index(
        'Country'
    )
    print(country_codes.loc['United_Kingdom']['Code'])
    for country_name in country_codes.index:
        country_files: list[str] = [
            data_file
            for data_file in os.listdir(select_output_folder)
            if data_file.startswith(country_name)
        ]
        country_files_with_code: list[str] = [
            country_file.replace(
                country_name, country_codes.loc[country_name]['Code']
            )
            for country_file in country_files
        ]
        for country_file, country_file_with_code in zip(
            country_files, country_files_with_code
        ):
            try:
                os.rename(
                    f'{select_output_folder}/{country_file}',
                    f'{select_output_folder}/{country_file_with_code}',
                )
            except FileExistsError:
                os.replace(
                    f'{select_output_folder}/{country_file}',
                    f'{select_output_folder}/{country_file_with_code}',
                )


if __name__ == '__main__':
    case_name: str = 'Mopo_industrial_case_study'
    ChaProEV.run_ChaProEV(case_name)
    print('Cooo')
    copy_select_files(case_name)
    rename_files_with_country_codes(case_name)
    print(
        ' line 81 in car home parking needs an if sessions and '
        'if generate profiles'
    )

# test use profile from net * effective effiicency (replace errors by zeros)


# Home-work distance from CBS for NL (either equivalent in BE or per urbanity)
# Car size NL/BE
# Woking time NL/BE

# Fleets from stats?

# Neeed inputs:
# Variants
# Fleets
# cars own driveway percentages

# Have NUTS 2 inputs
# Converted to IC1
# and put the latter in the files

#S s need an Excel with NUTS2 inoputs and conversion to IC1
# sm or avregae population or area basis

# Use NUTS2_IC1

# area or pop 
# 