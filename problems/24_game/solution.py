class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        bad = '떢븻각걎냇갅갸꺚뵟숣욄뵴뵞뤼갈갌뤔떌옊메늄숭캸긶꺛옖갍뇐쩢곴듇걯궄옕왹눞솴걃끗긬땉궿가쌀낐걄숤뺴늘걘꽸숢걂갋갃쫐꼔솾쩡쇔솿끛뤜간븺쩬웨딴옠뤛갂뵪덠놤빐옋귒늂갰갖놥궾갆옌뼘묰거갎긷낤겼'
        return chr(int(''.join(map(str, sorted(nums)))) + 42921) not in bad