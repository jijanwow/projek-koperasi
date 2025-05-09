import pandas as pd

def load_member_data(file_path):
    """
    Load koperasi member data from an Excel file.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing member data.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

def find_member_by_id(df, member_id):
    """
    Find member(s) in the DataFrame by ID.

    Args:
        df (pandas.DataFrame): DataFrame with member data.
        member_id (str): ID to search for.

    Returns:
        pandas.DataFrame: DataFrame filtered with matching member ID.
    """
    # Ensure the ID column exists. We guess column named 'ID' or 'id' (case-insensitive)
    id_cols = [col for col in df.columns if col.lower() == 'id' or col.lower().find('id') != -1]

    if not id_cols:
        print("No 'ID' column found in the Excel data.")
        return pd.DataFrame()  # empty

    id_col = id_cols[0]

    # Filter rows matching the member_id as string (strip spaces)
    filtered = df[df[id_col].astype(str).str.strip() == member_id.strip()]
    return filtered

def get_yes_no_input(prompt):
    """
    Get a strict yes/no input from user.

    Args:
        prompt (str): The prompt to display.

    Returns:
        bool: True for 'y', False for 'n'
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Sila masukkan 'y' untuk Ya atau 'n' untuk Tidak.")

def main():
    file_path = 'MultipleFiles/ahli_koperasi.xlsx'  # You can update this path
    df = load_member_data(file_path)
    if df is None:
        return

    print("Status Ahli Koperasi SMK BARU MIRI")

    while True:
        member_id = input("Sila isi nombor kad pengenalan: ").strip()

        result = find_member_by_id(df, member_id)

        if not result.empty:
            print(f"\nRekod dijumpai: {len(result)} rekod untuk ID ahli '{member_id}':\n")
            
            # Print all columns of the member record(s)
            print(result.to_string(index=False))
        else:
            print(f"\nRekod anda untuk '{member_id}' tidak dijumpai. Sila mendaftar sebagai ahli koperasi dengan berjumpa cikgu sulaiman.")

        # Ask if the user wants to continue or exit
        if not get_yes_no_input("\nAdakah anda ingin meneruskan? (y/n): "):
            print("Terima kasih!")
            break

if __name__ == '__main__':
    main()