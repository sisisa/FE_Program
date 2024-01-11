# 三角形クラスの定義
class Triangle:
    def __init__(self, bottom, height):
        # 三角形の底辺と高さを初期化
        self.bottom = bottom
        self.height = height
    
    # 三角形の面積を計算するメソッド
    def area(self):
        return self.bottom * self.height / 2

# 三角柱クラスの定義（Triangleクラスを継承）
class TrianglePole(Triangle):
    def __init__(self, bottom, height, tall):
        # 親クラスの初期化メソッドを呼び出し、三角形の底辺と高さを設定
        super().__init__(bottom, height)
        # 三角柱の高さを初期化
        self.tall = tall
    
    # 三角柱の体積を計算するメソッド
    def volume(self):
        # 親クラスの面積計算メソッドを呼び出し、それに三角柱の高さを掛けて体積を求める
        return self.area() * self.tall
