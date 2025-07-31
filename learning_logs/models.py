""" アプリに格納されるデータの扱い方を指示 
（フィールドの種類: https://docs.djangoproject.com/ja/5.2/ref/models/fields/）"""

from django.db import models

# Create your models here.
class Topic(models.Model):
  """ユーザーが学んでいるトピックを表す"""
  text = models.CharField(max_length=200) # 短い文字列を格納（上限文字数必須）
  date_added = models.DateTimeField(auto_now_add=True) # 日時を記録
  ' auto_now_add = ユーザが新トピック作成時、現在日時を自動で設定 '

  def __str__(self):
    """モデルの文字列表現を返す"""
    return self.text

class Entry(models.Model):
  """トピックに関して学んだ具体的なこと"""
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  ''' 外部キーのインスタンス（ データベース内の他レコードへの参照。ID割り振り。 ）
  CASCADE = トピックを削除した際、関連づいた記事も削除。 = カスケード削除 '''

  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    """モデルを管理するための追加情報"""
    verbose_name_plural = 'entries' # entryの複数形の表記を指定

  def __str__(self):
    """モデルの文字列表現を返す"""
    return f"{self.text[:25]}..." # 記事の本文の最初の25文字だけ表示
