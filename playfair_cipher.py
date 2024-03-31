
class PlayfairCipher:
    def __init__(self, key):
        self.key = self.process_key(key)
        self.matrix = self.generate_matrix(self.key)

    def process_key(self, key):
        # Xử lý khóa bằng cách loại bỏ ký tự trùng lặp và thay thế 'J' bằng 'I'
        key = key.upper().replace("J", "I")
        processed_key = ""
        for char in key:
            if char not in processed_key and char.isalpha():
                processed_key += char
        return processed_key

    def generate_matrix(self, key):
        # Tạo ma trận Playfair từ khóa
        matrix = ""
        for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in matrix:
                matrix += char
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(self, char):
        # Tìm vị trí của ký tự trong ma trận Playfair
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return i, j

    def decrypt(self, cipher_text):
        # Triển khai logic giải mã Playfair
        plain_text = ""
        for i in range(0, len(cipher_text), 2):
            char1 = cipher_text[i]
            char2 = cipher_text[i+1]
            position1 = self.find_position(char1)
            position2 = self.find_position(char2)
            if position1 is None or position2 is None:
                continue  # Bỏ qua các ký tự không tồn tại trong ma trận Playfair
            row1, col1 = position1
            row2, col2 = position2
            if row1 == row2:  # Cùng hàng
                plain_text += self.matrix[row1][(col1 - 1) % 5]
                plain_text += self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                plain_text += self.matrix[(row1 - 1) % 5][col1]
                plain_text += self.matrix[(row2 - 1) % 5][col2]
            else:  # Khác hàng và cột
                plain_text += self.matrix[row1][col2]
                plain_text += self.matrix[row2][col1]
        return plain_text

    def decode(self):
        key = self.key_entry.get().upper()
        cipher_text = self.input_entry.get().upper()
        if len(cipher_text) % 2 != 0:
            messagebox.showerror("Error", "Cipher text length must be even")
            return
        cipher = PlayfairCipher(key)
        plain_text = cipher.decrypt(cipher_text)
        self.output_text.delete(1.0, "end")
        self.output_text.insert("end", plain_text)

