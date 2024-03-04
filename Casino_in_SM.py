import pygame, random, sys, time

pygame.init()
screen_width = 1368
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) #가로 세로 설정
pygame.display.set_caption("Casino in SM") # 게임이름

# done = False  # 창이 꺼지지 않도록 함

clock = pygame.time.Clock()

#이미지 불러오기 -----------------------------------------------------

# 공용 이미지
chip_count = pygame.image.load("chip_count.png")



# 배경 이미지-----------------------------------------------------
bg_main = pygame.image.load("bg_main.png")
bg_credit = pygame.image.load("bg_credit.png")
bg_game_choice = pygame.image.load("bg_game_choice.png")
bg_gameover = pygame.image.load("bg_gameover.png")
bg_wrong = pygame.image.load("bg_wrong.png")

#슬롯 이미지
slot_jackpot = pygame.image.load("slot_jackpot.png")
slot_10 = pygame.image.load("slot_10.png")
slot_3 = pygame.image.load("slot_3.png")
slot_2 = pygame.image.load("slot_2.png")

bg_slotgame = pygame.image.load("bg_slotgame.png")
bg_gamerule_slotgame = pygame.image.load("bg_gamerule_slotgame.png")

#bg_slotgame_2 = pygame.image.load("bg_slotgame_2.png")
#bg_slotgame_3 = pygame.image.load("bg_slotgame_3.png")

#블랙잭 이미지
bg_gamerule_blackjack = pygame.image.load("bg_gamerule_blackjack.png")
bg_blackjack = pygame.image.load("bg_blackjack.png")

hit_img = pygame.image.load("hit.png")
stay_img = pygame.image.load("stay.png")
win_img = pygame.image.load("win.png")
lose_img = pygame.image.load("lose.png")
draw_img = pygame.image.load("draw.png")

#포커 이미지
bg_gamerule_poker = pygame.image.load("bg_gamerule_poker.png")
bg_gamerule_poker_2 = pygame.image.load("bg_gamerule_poker_2.png")
bg_poker = pygame.image.load("bg_poker.png")
fold_img = pygame.image.load("fold.png")
All_In_img = pygame.image.load("bt_start.png")


#다이사이 이미지
bg_gamerule_taisai = pygame.image.load("bg_gamerule_taisai.png")
bg_taisai = pygame.image.load("bg_taisai.png")
bg_taisai_result = pygame.image.load('bg_taisai_result.png')

#버튼 이미지---------------------------------------------------------
#공용
start_img = pygame.image.load("bt_start.png")
credit_img = pygame.image.load("bt_credit.png")
back_img = pygame.image.load("bt_back.png")
ok_img = pygame.image.load("bt_ok.png")
game_start_img = pygame.image.load("bt_start.png")
quit_img = pygame.image.load("bt_quit.png")

#슬롯 버튼 이미지
choice_slotgame_img = pygame.image.load("bt_slotgame_choice.png")
chip_up_img = pygame.image.load("bt_chip_up.png")
chip_10up_img = pygame.image.load("bt_10chips_up.png")
chip_down_img = pygame.image.load("bt_chip_down.png")
chip_10down_img = pygame.image.load("bt_10chips_down.png")

#블랙잭 버튼 이미지
choice_blackjack_img = pygame.image.load("bt_blackjack_choice.png")

#포커 버튼 이미지
choice_poker_img = pygame.image.load("bt_poker_choice.png")

#다이사이 버튼 이미지
choice_taisai_img = pygame.image.load("bt_taisai_choice.png")
taisai_game_start_img = pygame.image.load("bt_taisai_game_start.png")

#베팅 선택 버튼
big_small_img = pygame.image.load('bt_big_small.png')
even_odd_img = pygame.image.load('bt_even_odd.png')
pair_dice_img = pygame.image.load('bt_pair_dice.png')
any_triple_img = pygame.image.load('bt_any_triple.png')
triple_img = pygame.image.load('bt_triple.png')
single_dice_img = pygame.image.load('bt_single_dice.png')
hard_number_img = pygame.image.load('bt_hard_number.png')

big_small_select_img = pygame.image.load('bt_big_small_2.png')
even_odd_select_img = pygame.image.load('bt_even_odd_2.png')
pair_dice_select_img = pygame.image.load('bt_pair_dice_2.png')
any_triple_select_img = pygame.image.load('bt_any_triple_2.png')
triple_select_img = pygame.image.load('bt_triple_2.png')
single_dice_select_img = pygame.image.load('bt_single_dice_2.png')
hard_number_select_img = pygame.image.load('bt_hard_number_2.png')

#확인표시
bet_checked_img = pygame.image.load('bet_checked.png')
#베팅 1
big_img = pygame.image.load('bt_big.png')
small_img = pygame.image.load('bt_small.png')
big_select_img = pygame.image.load('bt_big_2.png')
small_select_img = pygame.image.load('bt_small_2.png')
#베팅 2
even_img = pygame.image.load('bt_even.png')
odd_img = pygame.image.load('bt_odd.png')
even_select_img = pygame.image.load('bt_even_2.png')
odd_select_img = pygame.image.load('bt_odd_2.png')
#주사위
dicenum1_img = pygame.image.load('dice_num1.png')
dicenum2_img = pygame.image.load('dice_num2.png')
dicenum3_img = pygame.image.load('dice_num3.png')
dicenum4_img = pygame.image.load('dice_num4.png')
dicenum5_img = pygame.image.load('dice_num5.png')
dicenum6_img = pygame.image.load('dice_num6.png')

dicenum1_select_img = pygame.image.load('dice_num1_2.png')
dicenum2_select_img = pygame.image.load('dice_num2_2.png')
dicenum3_select_img = pygame.image.load('dice_num3_2.png')
dicenum4_select_img = pygame.image.load('dice_num4_2.png')
dicenum5_select_img = pygame.image.load('dice_num5_2.png')
dicenum6_select_img = pygame.image.load('dice_num6_2.png')

#결과창 이미지
result_win_img = pygame.image.load('result_win.png')
result_lose_img = pygame.image.load('result_lose.png')
result_x_img = pygame.image.load('result_x.png')
result_dice1_img = pygame.image.load('result_dice1.png')
result_dice2_img = pygame.image.load('result_dice2.png')
result_dice3_img = pygame.image.load('result_dice3.png')
result_dice4_img = pygame.image.load('result_dice4.png')
result_dice5_img = pygame.image.load('result_dice5.png')
result_dice6_img = pygame.image.load('result_dice6.png')
result_winner_img = pygame.image.load('result_winner.png')

#카드 이미지---------------------------------------------------------

#For blackjack
cd_A = pygame.image.load("c_a.png")
cd_2 = pygame.image.load("c_2.png")
cd_3 = pygame.image.load("c_3.png")
cd_4 = pygame.image.load("c_4.png")
cd_5 = pygame.image.load("c_5.png")
cd_6 = pygame.image.load("c_6.png")
cd_7 = pygame.image.load("c_7.png")
cd_8 = pygame.image.load("c_8.png")
cd_9 = pygame.image.load("c_9.png")
cd_10 = pygame.image.load("c_10.png")
cd_J = pygame.image.load("c_j.png")
cd_K = pygame.image.load("c_k.png")
cd_Q = pygame.image.load("c_q.png")

#For poker

c_a = pygame.image.load("trump_cards\c_a.png")
c_a = pygame.transform.scale(c_a, (93, 127))
c_2 = pygame.image.load("trump_cards\c_2.png")
c_2 = pygame.transform.scale(c_2, (93, 127))
c_3 = pygame.image.load("trump_cards\c_3.png")
c_3 = pygame.transform.scale(c_3, (93, 127))
c_4 = pygame.image.load("trump_cards\c_4.png")
c_4 = pygame.transform.scale(c_4, (93, 127))
c_5 = pygame.image.load("trump_cards\c_5.png")
c_5 = pygame.transform.scale(c_5, (93, 127))
c_6 = pygame.image.load("trump_cards\c_6.png")
c_6 = pygame.transform.scale(c_6, (93, 127))
c_7 = pygame.image.load("trump_cards\c_7.png")
c_7 = pygame.transform.scale(c_7, (93, 127))
c_8 = pygame.image.load("trump_cards\c_8.png")
c_8 = pygame.transform.scale(c_8, (93, 127))
c_9 = pygame.image.load("trump_cards\c_9.png")
c_9 = pygame.transform.scale(c_9, (93, 127))
c_10 = pygame.image.load("trump_cards\c_10.png")
c_10 = pygame.transform.scale(c_10, (93, 127))
c_j = pygame.image.load("trump_cards\c_j.png")
c_j = pygame.transform.scale(c_j, (93, 127))
c_q = pygame.image.load("trump_cards\c_q.png")
c_q = pygame.transform.scale(c_q, (93, 127))
c_k = pygame.image.load("trump_cards\c_k.png")
c_k = pygame.transform.scale(c_k, (93, 127))

d_a = pygame.image.load("trump_cards\c_a.png")
d_a = pygame.transform.scale(d_a, (93, 127))
d_2 = pygame.image.load("trump_cards\c_2.png")
d_2 = pygame.transform.scale(d_2, (93, 127))
d_3 = pygame.image.load("trump_cards\c_3.png")
d_3 = pygame.transform.scale(d_3, (93, 127))
d_4 = pygame.image.load("trump_cards\c_4.png")
d_4 = pygame.transform.scale(d_4, (93, 127))
d_5 = pygame.image.load("trump_cards\c_5.png")
d_5 = pygame.transform.scale(d_5, (93, 127))
d_6 = pygame.image.load("trump_cards\c_6.png")
d_6 = pygame.transform.scale(d_6, (93, 127))
d_7 = pygame.image.load("trump_cards\c_7.png")
d_7 = pygame.transform.scale(d_7, (93, 127))
d_8 = pygame.image.load("trump_cards\c_8.png")
d_8 = pygame.transform.scale(d_8, (93, 127))
d_9 = pygame.image.load("trump_cards\c_9.png")
d_9 = pygame.transform.scale(d_9, (93, 127))
d_10 = pygame.image.load("trump_cards\c_10.png")
d_10 = pygame.transform.scale(d_10, (93, 127))
d_j = pygame.image.load("trump_cards\c_j.png")
d_j = pygame.transform.scale(d_j, (93, 127))
d_q = pygame.image.load("trump_cards\c_q.png")
d_q = pygame.transform.scale(d_q, (93, 127))
d_k = pygame.image.load("trump_cards\c_k.png")
d_k = pygame.transform.scale(d_k, (93, 127))

h_a = pygame.image.load("trump_cards\h_a.png")
h_a = pygame.transform.scale(h_a, (93, 127))
h_2 = pygame.image.load("trump_cards\h_2.png")
h_2 = pygame.transform.scale(h_2, (93, 127))
h_3 = pygame.image.load("trump_cards\h_3.png")
h_3 = pygame.transform.scale(h_3, (93, 127))
h_4 = pygame.image.load("trump_cards\h_4.png")
h_4 = pygame.transform.scale(h_4, (93, 127))
h_5 = pygame.image.load("trump_cards\h_5.png")
h_5 = pygame.transform.scale(h_5, (93, 127))
h_6 = pygame.image.load("trump_cards\h_6.png")
h_6 = pygame.transform.scale(h_6, (93, 127))
h_7 = pygame.image.load("trump_cards\h_7.png")
h_7 = pygame.transform.scale(h_7, (93, 127))
h_8 = pygame.image.load("trump_cards\h_8.png")
h_8 = pygame.transform.scale(h_8, (93, 127))
h_9 = pygame.image.load("trump_cards\h_9.png")
h_9 = pygame.transform.scale(h_9, (93, 127))
h_10 = pygame.image.load("trump_cards\h_10.png")
h_10 = pygame.transform.scale(h_10, (93, 127))
h_j = pygame.image.load("trump_cards\h_j.png")
h_j = pygame.transform.scale(h_j, (93, 127))
h_q = pygame.image.load("trump_cards\h_q.png")
h_q = pygame.transform.scale(h_q, (93, 127))
h_k = pygame.image.load("trump_cards\h_k.png")
h_k = pygame.transform.scale(h_k, (93, 127))

s_a = pygame.image.load("trump_cards\s_a.png")
s_a = pygame.transform.scale(s_a, (93, 127))
s_2 = pygame.image.load("trump_cards\s_2.png")
s_2 = pygame.transform.scale(s_2, (93, 127))
s_3 = pygame.image.load("trump_cards\s_3.png")
s_3 = pygame.transform.scale(s_3, (93, 127))
s_4 = pygame.image.load("trump_cards\s_4.png")
s_4 = pygame.transform.scale(s_4, (93, 127))
s_5 = pygame.image.load("trump_cards\s_5.png")
s_5 = pygame.transform.scale(s_5, (93, 127))
s_6 = pygame.image.load("trump_cards\s_6.png")
s_6 = pygame.transform.scale(s_6, (93, 127))
s_7 = pygame.image.load("trump_cards\s_7.png")
s_7 = pygame.transform.scale(s_7, (93, 127))
s_8 = pygame.image.load("trump_cards\s_8.png")
s_8 = pygame.transform.scale(s_8, (93, 127))
s_9 = pygame.image.load("trump_cards\s_9.png")
s_9 = pygame.transform.scale(s_9, (93, 127))
s_10 = pygame.image.load("trump_cards\s_10.png")
s_10 = pygame.transform.scale(s_10, (93, 127))
s_j = pygame.image.load("trump_cards\s_j.png")
s_j = pygame.transform.scale(s_j, (93, 127))
s_q = pygame.image.load("trump_cards\s_q.png")
s_q = pygame.transform.scale(s_q, (93, 127))
s_k = pygame.image.load("trump_cards\s_k.png")
s_k = pygame.transform.scale(s_k, (93, 127))

#숫자 이미지---------------------------------------------------------

one = pygame.image.load("one.png")
two = pygame.image.load("two.png")
three = pygame.image.load("three.png")
four = pygame.image.load("four.png")
five = pygame.image.load("five.png")
six = pygame.image.load("six.png")
seven = pygame.image.load("seven.png")
eight = pygame.image.load("eight.png")
nine = pygame.image.load("nine.png")

#버튼 클래스-------------------------------------
class Button:
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) #크기 조절
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y) #좌측 상단에서 그린다
		self.clicked = False

	def draw(self):
		button_action = False
		#마우스 위치 얻기
		pos = pygame.mouse.get_pos()

		#마우스 체크
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #마우스의 왼쪽으로 클릭했는가?
				self.clicked = True # 이렇게 투르 펄스로 해놓으면 버튼의 중복해서 누를 수 없음 / 다시  False로 안바꿔줬으니깐
				button_action = '1'

			if pygame.mouse.get_pressed()[2] == 1: # 우측 클릭
				self.clicked = True
				button_action = '2'

		if pygame.mouse.get_pressed()[0] == 0: # 여기서 클릭을 땠으면 다시 False로 바꿔줌
			self.clicked = False 

		#스크린에 버튼 그리기
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return button_action



#버튼 생성-----------------------------------------------------
#공용 버튼
start_button = Button(200, 370, start_img, 2)
credit_button = Button (200, 520, credit_img, 2)
back_button = Button(1305, 0, back_img, 0.5)
ok_button = Button(screen_width/2 - 50, 610, ok_img, 1)
quit_button = Button(1140, 620, quit_img, 1)

#슬롯 버튼
choice_slotgame_button = Button(570, 180, choice_slotgame_img, 2)

chip_up_button = Button(714, 314, chip_up_img, 0.6)
chip_10up_button = Button(714, 280, chip_10up_img, 0.6)
chip_down_button = Button(714, 385, chip_down_img, 0.6)
chip_10down_button = Button(714, 413, chip_10down_img, 0.6)

slotgame_start_button = Button(624, 475, game_start_img, 1)

#블랙잭 버튼
choice_blackjack_button = Button(850, 180, choice_blackjack_img, 2)

bj_chip_up_button = Button(1070, 615, chip_up_img, 0.6)
bj_chip_down_button = Button(1070, 645, chip_down_img, 0.6)
bj_start_button = Button(1140, 620, game_start_img, 1)
bj_back_button = Button(1235, 0, back_img, 1)
bj_stay_button = Button(560, 350, stay_img, 1)
bj_hit_button = Button(700, 350, hit_img, 1)

#포커 버튼
choice_poker_button = Button(570, 340, choice_poker_img, 2)
fold_button = Button(435, 600, fold_img, 1)

po_start_button = Button(1140, 620, game_start_img, 1)
po_chip_up_button = Button(1070, 615, chip_up_img, 0.6)
po_chip_down_button = Button(1070, 645, chip_down_img, 0.6)

#다이사이 버튼
choice_taisai_button = Button(850, 340, choice_taisai_img, 2)
taisai_start_button = Button(1200, 600, taisai_game_start_img, 1)

#베팅 선택 버튼
big_small_button = Button(21, 30, big_small_img, 1)
even_odd_button = Button(363, 30, even_odd_img, 1)
pair_dice_button = Button(705, 30, pair_dice_img, 1)
any_triple_button = Button(1047, 30, any_triple_img, 1)
triple_button = Button(21, 390, triple_img, 1)
single_dice_button = Button(363, 390, single_dice_img, 1)
hard_number_button = Button(705, 390, hard_number_img, 1)

big_small_select_button = Button(21, 30, big_small_select_img, 1)
even_odd_select_button = Button(363, 30, even_odd_select_img, 1)
pair_dice_select_button = Button(705, 30, pair_dice_select_img, 1)
any_triple_select_button = Button(1047, 30, any_triple_select_img, 1)
triple_select_button = Button(21, 390, triple_select_img, 1)
single_dice_select_button = Button(363, 390, single_dice_select_img, 1)
hard_number_select_button = Button(705, 390, hard_number_select_img, 1)

#game 1
big_button = Button(30, 250, big_img, 1)
small_button = Button(182, 250, small_img, 1)
big_select_button = Button(30, 250, big_select_img, 1)
samll_select_button = Button(30, 250, small_select_img, 1)

#game 2
even_button = Button(372, 250, even_img, 1)
odd_button = Button(524, 250, odd_img, 1)
even_select_button = Button(372, 250, even_select_img, 1)
odd_select_button = Button(524, 250, odd_select_img, 1)

#game 3
game3_dicenum1_button = Button(754, 230, dicenum1_img, 1)
game3_dicenum2_button = Button(830, 230, dicenum2_img, 1)
game3_dicenum3_button = Button(906, 230, dicenum3_img, 1)
game3_dicenum4_button = Button(754, 300, dicenum4_img, 1)
game3_dicenum5_button = Button(830, 300, dicenum5_img, 1)
game3_dicenum6_button = Button(906, 300, dicenum6_img, 1)

game3_dicenum1_select_button = Button(754, 230, dicenum1_select_img, 1)
game3_dicenum2_select_button = Button(830, 230, dicenum2_select_img, 1)
game3_dicenum3_select_button = Button(906, 230, dicenum3_select_img, 1)
game3_dicenum4_select_button = Button(754, 300, dicenum4_select_img, 1)
game3_dicenum5_select_button = Button(830, 300, dicenum5_select_img, 1)
game3_dicenum6_select_button = Button(906, 300, dicenum6_select_img, 1)

#베팅4
game4_dicenum1_button = Button(1096, 230, dicenum1_img, 1)
game4_dicenum2_button = Button(1172, 230, dicenum2_img, 1)
game4_dicenum3_button = Button(1248, 230, dicenum3_img, 1)
game4_dicenum4_button = Button(1096, 300, dicenum4_img, 1)
game4_dicenum5_button = Button(1172, 300, dicenum5_img, 1)
game4_dicenum6_button = Button(1248, 300, dicenum6_img, 1)

game4_dicenum1_select_button = Button(1096, 230, dicenum1_select_img, 1)
game4_dicenum2_select_button = Button(1172, 230, dicenum2_select_img, 1)
game4_dicenum3_select_button = Button(1248, 230, dicenum3_select_img, 1)
game4_dicenum4_select_button = Button(1096, 300, dicenum4_select_img, 1)
game4_dicenum5_select_button = Button(1172, 300, dicenum5_select_img, 1)
game4_dicenum6_select_button = Button(1248, 300, dicenum6_select_img, 1)

#베팅5
game5_dicenum1_button = Button(70, 590, dicenum1_img, 1)
game5_dicenum2_button = Button(146, 590, dicenum2_img, 1)
game5_dicenum3_button = Button(222, 590, dicenum3_img, 1)
game5_dicenum4_button = Button(70, 660, dicenum4_img, 1)
game5_dicenum5_button = Button(146, 660, dicenum5_img, 1)
game5_dicenum6_button = Button(222, 660, dicenum6_img, 1)

game5_dicenum1_select_button = Button(70, 590,  dicenum1_select_img, 1)
game5_dicenum2_select_button = Button(146, 590, dicenum2_select_img, 1)
game5_dicenum3_select_button = Button(222, 590, dicenum3_select_img, 1)
game5_dicenum4_select_button = Button(70, 660,  dicenum4_select_img, 1)
game5_dicenum5_select_button = Button(146, 660, dicenum5_select_img, 1)
game5_dicenum6_select_button = Button(222, 660, dicenum6_select_img, 1)

#베팅7
game7_dicenum1_button = Button(754, 590, dicenum1_img, 1)
game7_dicenum2_button = Button(830, 590, dicenum2_img, 1)
game7_dicenum3_button = Button(906, 590, dicenum3_img, 1)
game7_dicenum4_button = Button(754, 660, dicenum4_img, 1)
game7_dicenum5_button = Button(830, 660, dicenum5_img, 1)
game7_dicenum6_button = Button(906, 660, dicenum6_img, 1)

game7_dicenum1_select_button = Button(754, 590, dicenum1_select_img, 1)
game7_dicenum2_select_button = Button(830, 590, dicenum2_select_img, 1)
game7_dicenum3_select_button = Button(906, 590, dicenum3_select_img, 1)
game7_dicenum4_select_button = Button(754, 660, dicenum4_select_img, 1)
game7_dicenum5_select_button = Button(830, 660, dicenum5_select_img, 1)
game7_dicenum6_select_button = Button(906, 660, dicenum6_select_img, 1)

#다이사이 배팅버튼
#베팅1
chip_up_button1 = Button(230, 115, chip_up_img, 0.5)
chip10_up_button1 = Button(230, 85, chip_10up_img, 0.5)
chip_down_button1 = Button(230, 180, chip_down_img, 0.5)
chip10_down_button1 = Button(230, 175, chip_10down_img, 0.5)

#베팅2
chip_up_button2 = Button(572, 115, chip_up_img, 0.5)
chip10_up_button2 = Button(572, 85, chip_10up_img, 0.5)
chip_down_button2 = Button(572, 180, chip_down_img, 0.5)
chip10_down_button2 = Button(572, 175, chip_10down_img, 0.5)

#베팅3
chip_up_button3 = Button(914, 115, chip_up_img, 0.5)
chip10_up_button3 = Button(914, 85, chip_10up_img, 0.5)
chip_down_button3 = Button(914, 180, chip_down_img, 0.5)
chip10_down_button3 = Button(914, 175, chip_10down_img, 0.5)

#베팅4
chip_up_button4 = Button(1256, 115, chip_up_img, 0.5)
chip10_up_button4 = Button(1256, 85, chip_10up_img, 0.5)
chip_down_button4 = Button(1256, 180, chip_down_img, 0.5)
chip10_down_button4 = Button(1256, 175, chip_10down_img, 0.5)

#베팅5
chip_up_button5 = Button(230, 480, chip_up_img, 0.5)
chip10_up_button5 = Button(230, 445, chip_10up_img, 0.5)
chip_down_button5 = Button(230, 545, chip_down_img, 0.5)
chip10_down_button5 = Button(230, 535, chip_10down_img, 0.5)

#베팅6
chip_up_button6 = Button(572, 480, chip_up_img, 0.5)
chip10_up_button6 = Button(572, 445, chip_10up_img, 0.5)
chip_down_button6 = Button(572, 545, chip_down_img, 0.5)
chip10_down_button6 = Button(572, 535, chip_10down_img, 0.5)

#베팅7
chip_up_button7 = Button(914, 480, chip_up_img, 0.5)
chip10_up_button7 = Button(914, 445, chip_10up_img, 0.5)
chip_down_button7 = Button(914, 545, chip_down_img, 0.5)
chip10_down_button7 = Button(914, 535, chip_10down_img, 0.5)

taisai_back_button = Button(1305, 657, back_img, 0.5)


#----------------------------------------------------------

screen.blit(bg_main, (0, 0)) #배경 그리기 (배경 이름, 위치좌표)


#변수들-----------------------------------------------------
#공통 변수
bg_name = 'bg_main'
chip = 10
input_chip = 0

#슬롯 변수
state = "S"
result_list = []

#블랙잭 변수
repeat = True
stayOrhit = 0
blackjack_state = " "
chip_state = " "
playerIn = True
dealerIn = True
deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']
playerhand = []
dealerhand = []


#포커 변수
repeat = True
Deck = []
Player1 = []
Player2 = []

#다이사이 변수
#이 게임에 베팅할 칩 갯수
game_num = []
game1_numlist = []
game2_numlist = []
game3_numlist = []
game4_numlist = []
game5_numlist = []
game7_numlist = []

game1_chip = 0
game2_chip = 0
game3_chip = 0
game4_chip = 0
game5_chip = 0
game6_chip = 0
game7_chip = 0

result1 = ' '
result2 = ' '
result3 = ' '
result4 = ' '
result5 = ' '
result6 = ' '
result7 = ' '

s3 = 0
s4 = 0
s7 = 0

#게임-------------------------------------------------------

#칩 초기화 함수
def clear_chip():
	global input_chip
	input_chip = 0
#슬롯-------------------------------------------------------

def slotgame_mix_num():
	num_list = [one, two, three, four, five, six, seven, eight, nine]
	for i in range(random.randint(35, 50)):
		pygame.time.delay(30)

		screen.blit(num_list[random.randint(0, 8)], (433, 290))
		screen.blit(num_list[random.randint(0, 8)], (613, 290))
		screen.blit(num_list[random.randint(0, 8)], (793, 290))

		pygame.display.update()

def slotgame_print_num(slot_num):
	for i in range(0, 3):
		if i == 0:
			x = 433
		elif i == 1:
			x = 613
		elif i == 2:
			x = 793
		if slot_num[i] == 1:
			screen.blit(one, (x, 290))
		elif slot_num[i] == 2:
			screen.blit(two, (x, 290))
		elif slot_num[i] == 3:
			screen.blit(three, (x, 290))
		elif slot_num[i] == 4:
			screen.blit(four, (x, 290))
		elif slot_num[i] == 5:
			screen.blit(five, (x, 290))
		elif slot_num[i] == 6:
			screen.blit(six, (x, 290))
		elif slot_num[i] == 7:
			screen.blit(seven, (x, 290))
		elif slot_num[i] == 8:
			screen.blit(eight, (x, 290))
		elif slot_num[i] == 9:
			screen.blit(nine, (x, 290))
		pygame.display.update()

def slotgame(chip, input_chip):
	num = []

	chip = chip - input_chip

	for i in range(0, 3): 
		num.append(random.randint(1, 9))

	if (num[0] == num[1] and num[1] == num[2] and num[2] == num[0]):
		if(num[0] == 7):
			slotgame_mix_num()
			slotgame_print_num(num)
			screen.blit(slot_jackpot, (200, 100)) 
			pygame.display.update()
			pygame.time.delay(5000)
			return chip + input_chip * 100, num
		else:
			slotgame_mix_num()
			slotgame_print_num(num)
			screen.blit(slot_10, (200, 100))
			pygame.display.update()
			pygame.time.delay(3000)
			return chip + input_chip * 10, num
	elif(num[0] == num[1] or num[1] == num[2] or num[2] == num[0]):
		if (num.count(7) == 2):
			slotgame_mix_num()
			slotgame_print_num(num)
			screen.blit(slot_3, (200, 100))
			pygame.display.update()
			pygame.time.delay(2500)
			return chip + input_chip * 3, num
		else:
			slotgame_mix_num()
			slotgame_print_num(num)
			screen.blit(slot_2, (200, 100))
			pygame.display.update()
			pygame.time.delay(2000)
			return chip + input_chip * 2, num
	else:
		slotgame_mix_num()
		slotgame_print_num(num)
		pygame.time.delay(2000)
		return chip, num

#블랙잭
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
#각각의 패의 합 계산
def total(turn) :
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    pygame.display.update()
    return total
#승자 확인
def revealDealerhand():
    if len(dealerhand) == 2:
        if dealerhand[0] == 2:
                screen.blit(cd_2, (65, 165))
        elif dealerhand[0] == 3:
                screen.blit(cd_3, (65, 165))
        elif dealerhand[0] == 4:
                screen.blit(cd_4, (65, 165))
        elif dealerhand[0] == 5:
                screen.blit(cd_5, (65, 165))
        elif dealerhand[0] == 6:
                screen.blit(cd_6, (65, 165))
        elif dealerhand[0] == 7:
                screen.blit(cd_7, (65, 165))
        elif dealerhand[0] == 8:
                screen.blit(cd_8, (65, 165))
        elif dealerhand[0] == 9:
                screen.blit(cd_9, (65, 165))
        elif dealerhand[0] == 10:
                screen.blit(cd_10, (65, 165))
        elif dealerhand[0] == 'J':
                screen.blit(cd_J, (65, 165))
        elif dealerhand[0] == 'K':
                screen.blit(cd_K, (65, 165))
        elif dealerhand[0] == 'Q':
                screen.blit(cd_Q, (65, 165))
        elif dealerhand[0] == 'A':
                screen.blit(cd_A, (65, 165))    
        pygame.display.update()
        return dealerhand[0]
    elif len(dealerhand) > 2:
        for i in range(2):
            if i == 0:
                x = 65 
            elif i == 1:
                x = 170
            if dealerhand[i] == 2:
                screen.blit(cd_2, (x, 165))
            elif dealerhand[i] == 3:
                screen.blit(cd_3, (x, 165))
            elif dealerhand[i] == 4:
                screen.blit(cd_4, (x, 165))
            elif dealerhand[i] == 5:
                screen.blit(cd_5, (x, 165))
            elif dealerhand[i] == 6:
                screen.blit(cd_6, (x, 165))
            elif dealerhand[i] == 7:
                screen.blit(cd_7, (x, 165))
            elif dealerhand[i] == 8:
                screen.blit(cd_8, (x, 165))
            elif dealerhand[i] == 9:
                screen.blit(cd_9, (x, 165))
            elif dealerhand[i] == 10:
                screen.blit(cd_10, (x, 165))
            elif dealerhand[i] == 'J':
                screen.blit(cd_J, (x, 165))
            elif dealerhand[i] == 'K':
                screen.blit(cd_K, (x, 165))
            elif dealerhand[i] == 'Q':
                screen.blit(cd_Q, (x, 165))
            elif dealerhand[i] == 'A':
                screen.blit(cd_A, (x, 165))
            pygame.display.update()
        return dealerhand[0], dealerhand[1]
#게임 루프
def blackjack():
    

    for i in range(2):
        dealCard(dealerhand)
        dealCard(playerhand)
    for i in range(2):
        if i == 0:
            x = 65
        elif i == 1:
            x = 170
        if playerhand[i] == 2:
            screen.blit(cd_2, (x, 420))
        elif playerhand[i] == 3:
            screen.blit(cd_3, (x, 420))
        elif playerhand[i] == 4:
            screen.blit(cd_4, (x, 420))
        elif playerhand[i] == 5:
            screen.blit(cd_5, (x, 420))
        elif playerhand[i] == 6:
            screen.blit(cd_6, (x, 420))
        elif playerhand[i] == 7:
            screen.blit(cd_7, (x, 420))
        elif playerhand[i] == 8:
            screen.blit(cd_8, (x, 420))
        elif playerhand[i] == 9:
            screen.blit(cd_9, (x, 420))
        elif playerhand[i] == 10:
            screen.blit(cd_10, (x, 420))
        elif playerhand[i] == 'J':
            screen.blit(cd_J, (x, 420))
        elif playerhand[i] == 'K':
            screen.blit(cd_K, (x, 420))
        elif playerhand[i] == 'Q':
            screen.blit(cd_Q, (x, 420))
        elif playerhand[i] == 'A':
            screen.blit(cd_A, (x, 420))
        pygame.display.update()

    revealDealerhand()
    pygame.display.update()

def result():
	global playerhand
	global dealerhand
	global deck
	global blackjack_state
	global chip_state
	if total(playerhand) == 21:
		screen.blit(win_img,(430, 200))
		pygame.display.update()
		pygame.time.delay(3000)
		blackjack_state = " "
		chip_state = "clear"
		screen.blit(bg_blackjack,(0, 0))
		playerhand = []
		dealerhand = []
		deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']

		pygame.display.update()
		return 5
	elif total(dealerhand) == 21:
		screen.blit(lose_img,(430, 200))
		pygame.display.update()
		pygame.time.delay(3000)
		blackjack_state = " "
		chip_state = "clear"
		screen.blit(bg_blackjack,(0, 0))
		playerhand = []
		dealerhand = []
		deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']

		pygame.display.update()
		return 0
	elif total(playerhand) > 21:
		screen.blit(lose_img,(430, 200))
		pygame.display.update()
		pygame.time.delay(3000)
		blackjack_state = " "
		chip_state = "clear"
		screen.blit(bg_blackjack,(0, 0))
		playerhand = []
		dealerhand = []
		deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']

		pygame.display.update()
		return 0
	elif total(dealerhand) > 21:
		screen.blit(win_img,(430, 200))
		pygame.display.update()
		pygame.time.delay(3000)
		blackjack_state = " "
		chip_state = "clear"
		screen.blit(bg_blackjack,(0, 0))
		playerhand = []
		dealerhand = []
		deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']

		pygame.display.update()
		return 2
	elif 21 - total(dealerhand) < 21 - total(playerhand):
		screen.blit(lose_img,(430, 200))
		pygame.display.update()
		pygame.time.delay(3000)
		blackjack_state = " "
		chip_state = "clear"
		screen.blit(bg_blackjack,(0, 0))
		playerhand = []
		dealerhand = []
		deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']

		pygame.display.update()
		return 0
	elif 21 - total(dealerhand) > 21 - total(playerhand):
		screen.blit(win_img,(430, 200))
		pygame.display.update()
		pygame.time.delay(3000)
		blackjack_state = " "
		chip_state = "clear"
		screen.blit(bg_blackjack,(0, 0))
		playerhand = []
		dealerhand = []
		deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']

		pygame.display.update()
		return 2
	elif 21 - total(dealerhand) == 21 - total(playerhand):
		screen.blit(draw_img,(430, 200))
		pygame.display.update()
		pygame.time.delay(3000)
		blackjack_state = " "
		chip_state = "clear"
		screen.blit(bg_blackjack,(0, 0))
		playerhand = []
		dealerhand = []
		deck = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']

		pygame.display.update()
		return 1

def choose_hit():
	global playerIn
	dealCard(playerhand)
	if playerhand[(len(playerhand) - 1)] == 2:
		screen.blit(cd_2, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 3:
		screen.blit(cd_3, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 4:
		screen.blit(cd_4, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 5:
		screen.blit(cd_5, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 6:
		screen.blit(cd_6, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 7:
		screen.blit(cd_7, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 8:
		screen.blit(cd_8, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 9:
		screen.blit(cd_9, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 10:
		screen.blit(cd_10, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 'J':
		screen.blit(cd_J, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 'K':
		screen.blit(cd_K, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 'Q':
		screen.blit(cd_Q, (65 + (105 * (len(playerhand) - 1)), 420))
	elif playerhand[(len(playerhand) - 1)] == 'A':
		screen.blit(cd_A, (65 + (105 * (len(playerhand) - 1)), 420))
	pygame.display.update()


	if total(playerhand) >= 21:
		prize = result()
		return str(prize)

def choose_stay():
    global playerIn
    while playerIn:
        if total(dealerhand) < 16:
            dealCard(dealerhand)
        else:
            playerIn = False
    playerIn = True

    for i in range(1, len(dealerhand)):
            if dealerhand[i] == 2:
                screen.blit(cd_2, (65 + (105 * i), 165))
            elif dealerhand[i] == 3:
                screen.blit(cd_3, (65 + (105 * i), 165))
            elif dealerhand[i] == 4:
                screen.blit(cd_4, (65 + (105 * i), 165))
            elif dealerhand[i] == 5:
                screen.blit(cd_5, (65 + (105 * i), 165))
            elif dealerhand[i] == 6:
                screen.blit(cd_6, (65 + (105 * i), 165))
            elif dealerhand[i] == 7:
                screen.blit(cd_7, (65 + (105 * i), 165))
            elif dealerhand[i] == 8:
                screen.blit(cd_8, (65 + (105 * i), 165))
            elif dealerhand[i] == 9:
                screen.blit(cd_9, (65 + (105 * i), 165))
            elif dealerhand[i] == 10:
                screen.blit(cd_10, (65 + (105 * i), 165))
            elif dealerhand[i] == 'J':
                screen.blit(cd_J, (65 + (105 * i), 165))
            elif dealerhand[i] == 'K':
                screen.blit(cd_K, (65 + (105 * i), 165))
            elif dealerhand[i] == 'Q':
                screen.blit(cd_Q, (65 + (105 * i), 165))
            elif dealerhand[i] == 'A':
                screen.blit(cd_A, (65 + (105 * i), 165))
            pygame.display.update()
    prize = result()
    return str(prize)


#포커
def MakeDeck(n):
	for i in range(1, 14):
		Deck.append((n, i))

def ShuffleDeck(deck):
    random.shuffle(deck)

#카드 이미지 구현
def card_img(Player1, i, x, y): # 사용자, 몇번째, 위치값 x, 위치값 y
	#클로버
	if Player1[i] == ('Clover', 1):
		screen.blit(c_a, (x, y))
	elif Player1[i] == ('Clover', 2):
		screen.blit(c_2, (x, y))
	elif Player1[i] == ('Clover', 3):
		screen.blit(c_3, (x, y))
	elif Player1[i] == ('Clover', 4):
		screen.blit(c_4, (x, y))
	elif Player1[i] == ('Clover', 5):
		screen.blit(c_5, (x, y))
	elif Player1[i] == ('Clover', 6):
		screen.blit(c_6, (x, y))
	elif Player1[i] == ('Clover', 7):
		screen.blit(c_7, (x, y))
	elif Player1[i] == ('Clover', 8):
		screen.blit(c_8, (x, y))
	elif Player1[i] == ('Clover', 9):
		screen.blit(c_9, (x, y))
	elif Player1[i] == ('Clover', 10):
		screen.blit(c_10, (x, y))
	elif Player1[i] == ('Clover', 11):
		screen.blit(c_j, (x, y))
	elif Player1[i] == ('Clover', 12):
		screen.blit(c_q, (x, y))
	elif Player1[i] == ('Clover', 13):
		screen.blit(c_k, (x, y))
	#스페이스
	elif Player1[i] == ('Space', 1):
		screen.blit(s_a, (x, y))
	elif Player1[i] == ('Space', 2):
		screen.blit(s_2, (x, y))
	elif Player1[i] == ('Space', 3):
		screen.blit(s_3, (x, y))
	elif Player1[i] == ('Space', 4):
		screen.blit(s_4, (x, y))
	elif Player1[i] == ('Space', 5):
		screen.blit(s_5, (x, y))
	elif Player1[i] == ('Space', 6):
		screen.blit(s_6, (x, y))
	elif Player1[i] == ('Space', 7):
		screen.blit(s_7, (x, y))
	elif Player1[i] == ('Space', 8):
		screen.blit(s_8, (x, y))
	elif Player1[i] == ('Space', 9):
		screen.blit(s_9, (x, y))
	elif Player1[i] == ('Space', 10):
		screen.blit(s_10, (x, y))
	elif Player1[i] == ('Space', 11):
		screen.blit(s_j, (x, y))
	elif Player1[i] == ('Space', 12):
		screen.blit(s_q, (x, y))
	elif Player1[i] == ('Space', 13):
		screen.blit(s_k, (x, y))
	#하트
	elif Player1[i] == ('Heart', 1):
		screen.blit(h_a, (x, y))
	elif Player1[i] == ('Heart', 2):
		screen.blit(h_2, (x, y))
	elif Player1[i] == ('Heart', 3):
		screen.blit(h_3, (x, y))
	elif Player1[i] == ('Heart', 4):
		screen.blit(h_4, (x, y))
	elif Player1[i] == ('Heart', 5):
		screen.blit(h_5, (x, y))
	elif Player1[i] == ('Heart', 6):
		screen.blit(h_6, (x, y))
	elif Player1[i] == ('Heart', 7):
		screen.blit(h_7, (x, y))
	elif Player1[i] == ('Heart', 8):
		screen.blit(h_8, (x, y))
	elif Player1[i] == ('Heart', 9):
		screen.blit(h_9, (x, y))
	elif Player1[i] == ('Heart', 10):
		screen.blit(h_10, (x, y))
	elif Player1[i] == ('Heart', 11):
		screen.blit(h_j, (x, y))
	elif Player1[i] == ('Heart', 12):
		screen.blit(h_q, (x, y))
	elif Player1[i] == ('Heart', 13):
		screen.blit(h_k, (x, y))
	#다이아몬드
	elif Player1[i] == ('Diamond', 1):
		screen.blit(d_a, (x, y))
	elif Player1[i] == ('Diamond', 2):
		screen.blit(d_2, (x, y))
	elif Player1[i] == ('Diamond', 3):
		screen.blit(d_3, (x, y))
	elif Player1[i] == ('Diamond', 4):
		screen.blit(d_4, (x, y))
	elif Player1[i] == ('Diamond', 5):
		screen.blit(d_5, (x, y))
	elif Player1[i] == ('Diamond', 6):
		screen.blit(d_6, (x, y))
	elif Player1[i] == ('Diamond', 7):
		screen.blit(d_7, (x, y))
	elif Player1[i] == ('Diamond', 8):
		screen.blit(d_8, (x, y))
	elif Player1[i] == ('Diamond', 9):
		screen.blit(d_9, (x, y))
	elif Player1[i] == ('Diamond', 10):
		screen.blit(d_10, (x, y))
	elif Player1[i] == ('Diamond', 11):
		screen.blit(d_j, (x, y))
	elif Player1[i] == ('Diamond', 12):
		screen.blit(d_q, (x, y))
	elif Player1[i] == ('Diamond', 13):
		screen.blit(d_k, (x, y))

def FirstOfShareCard(Player1, Player2, deck): #게임 내에서 한번에 5장을 받을 경우 (올인)
	for k in range(0, 5):
		Player1.append(deck[k])
	for k in range(5, 10):
		Player2.append(deck[k])

#승부 정하기 ------------------------------------------------------------
def WinOrLose(Player):
	pair = 0
	for m in range(0,4):
		for n in range(m+1, 5):
			if Player[m][1] == Player[n][1]:
				pair += 1

	player_Scard = []
	for i in range(0, 5):
		player_Scard.append(Player[i][1])
	player_Scard.sort()
	straight = False
	if pair == 0:
		if (player_Scard[4] - player_Scard[0]) == 4:
			straight == True
		if player_Scard[0] == 1 and player_Scard[1] == 10:
			straight == True

	player_Fcard = []        
	for i in range(0, 5):
		player_Fcard.append(Player[i][0])
	player_Fcard.sort()
	flush = False
	if player_Fcard[0] == player_Fcard[4]:
		flush = True

	if straight == True and flush == True:
		number = 1
	elif pair == 6:
		number = 2
	elif pair == 4:
		number = 3
	elif flush:
		number = 4
	elif straight:
		number = 5
	elif pair == 3:
		number = 6
	elif pair == 2:
		number = 7
	elif pair == 1:
		number = 8
	else:
		number = 9
	return number

def PlayOfGame():
	stage = 0

	random.shuffle(Deck)
	global chip
	global Player1
	global Player2
	global input_chip
	global bg_name

	if input_chip > 0 :
		if po_start_button.draw(): # 게임이 끝난 후에 카드가 섞이는 것과 카드 게임 재시작
			chip = chip - input_chip
			screen.blit(bg_poker, (0, 0))
			pygame.display.update()
			FirstOfShareCard(Player1, Player2, Deck)
			card_img(Player1, 0, 484, 170)
			card_img(Player1, 1, 587, 170)
			card_img(Player1, 2, 690, 170)
			card_img(Player1, 3, 793, 170)
			card_img(Player1, 4, 896, 170)
			card_img(Player2, 0, 483, 423)
			card_img(Player2, 1, 586, 423)
			card_img(Player2, 2, 689, 423)
			card_img(Player2, 3, 792, 423)
			card_img(Player2, 4, 895, 423)

			ResultOfPlayer1 = WinOrLose(Player1)
			ResultOfPlayer2 = WinOrLose(Player2)
			if ResultOfPlayer1 > ResultOfPlayer2:
				font = pygame.font.SysFont("맑은 고딕", 60)
				text_winner = font.render("Player Win!!", True, (255, 255, 0))
				screen.blit(text_winner, (575, 335))
				chip = chip + input_chip * 3
				input_chip = 0
				pygame.display.update()
				Player1 = [Deck[0], Deck[1]]
				Player2 = [Deck[2], Deck[3]]
				pygame.time.delay(5000)


			elif ResultOfPlayer1 == ResultOfPlayer2:
				font = pygame.font.SysFont("맑은 고딕", 60)
				text_winner = font.render("Draw!!", True, (255, 255, 0))
				screen.blit(text_winner, (630, 335))
				chip = chip + input_chip - 1
				input_chip = 0
				pygame.display.update()
				Player1 = [Deck[0], Deck[1]]
				Player2 = [Deck[2], Deck[3]]
				pygame.time.delay(5000)
				screen.blit(bg_poker, (0, 0))
				pygame.display.update()
				if chip == 0:
					screen.blit(bg_gameover, (0, 0))
					bg_name = "bg_gameover"
				else:
					screen.blit(bg_poker, (0, 0))
					pygame.display.update()

			else:
				font = pygame.font.SysFont("맑은 고딕", 60)
				text_winner = font.render("Computer Win!!", True, (255, 255, 0))
				screen.blit(text_winner, (545, 335))
				input_chip = 0
				pygame.display.update()
				Player1 = [Deck[0], Deck[1]]
				Player2 = [Deck[2], Deck[3]]
				pygame.time.delay(5000)
				screen.blit(bg_poker, (0, 0))
				pygame.display.update()
				if chip == 0:
					screen.blit(bg_gameover, (0, 0))
					bg_name = "bg_gameover"
				else:
					screen.blit(bg_poker, (0, 0))
					pygame.display.update()

def poker():

	Deck = []
	MakeDeck("Space")
	MakeDeck("Heart")
	MakeDeck("Clover")
	MakeDeck("Diamond")

	Player1 = []
	Player2 = [] 
	PlayOfGame()

#다이사이
def taisai_print_dice(dice_num):
	for i in range(0, 3):
		if i == 0:
			x = 1037
		elif i == 1:
			x = 1147
		elif i == 2:
			x = 1257
		if dice_num[i] == 1:
			screen.blit(result_dice1_img, (x, 290))
		elif dice_num[i] == 2:
			screen.blit(result_dice2_img, (x, 290))
		elif dice_num[i] == 3:
			screen.blit(result_dice3_img, (x, 290))
		elif dice_num[i] == 4:
			screen.blit(result_dice4_img, (x, 290))
		elif dice_num[i] == 5:
			screen.blit(result_dice5_img, (x, 290))
		elif dice_num[i] == 6:
			screen.blit(result_dice6_img, (x, 290))
		pygame.display.update()

def taisai_del():
	del game_num[0:]
	del game1_numlist[0:]
	del game2_numlist[0:]
	del game3_numlist[0:]
	del game4_numlist[0:]
	del game5_numlist[0:]
	del game7_numlist[0:]

	#이 게임에 베팅할 칩 갯수
	game1_chip = 0
	game2_chip = 0
	game3_chip = 0
	game4_chip = 0
	game5_chip = 0
	game6_chip = 0
	game7_chip = 0


	s3 = 0
	s4 = 0
	s7 = 0

	result1 = ' '
	result2 = ' '
	result3 = ' '
	result4 = ' '
	result5 = ' '
	result6 = ' '
	result7 = ' '
	
def taisai_dice_selection(): #주사위 고르는 함수 스타트 버튼으로 시작할 예정

	dice_num1 = random.randint(1, 6)
	dice_num2 = random.randint(1, 6)
	dice_num3 = random.randint(1, 6)
	dice_numlist = [dice_num1, dice_num2, dice_num3]      # 주사위조합
	sum_dice = dice_num1 + dice_num2 + dice_num3     # 주사위 합

	return dice_numlist, sum_dice

def taisai_big_small_game(sum_dice): # 첫번째 게임은 다이스의 합을 비교해 리턴

	if 1 in game_num: #게임 참여 여부
			if 11 <= sum_dice <= 17:
				if game1_numlist[0] == 1:
					result1 = 'You Win'
				else:
					result1 = 'You Lose'
			elif 4 <= sum_dice <= 10:
				if game1_numlist[0] == 2:
					result1 = 'You Win'
				else:
					result1 = 'You Lose'
			else:
				result1 = 'You Lose'
	else:
		result1 = '참여 X'

	return result1

def taisai_even_odd_game(sum_dice): #다이스의 총 합을 받아 짝홀 리턴
	if 2 in game_num:
		if sum_dice % 2 == 0:
			if game2_numlist[0] == 1:
				result2 = 'You Win'
			else :
				result2 = 'You Lose'
		else :
			if game2_numlist[0] == 2:
				result2 = 'You Win'
			else :
				result2 = 'You Lose'
	else :
		result2 = '참여 X'

	return result2

def taisai_pair_dice_game(game3_numlist, dice_numlist): #내가 선택한 주사위와 랜덤 주사위 배열 입력
	if 3 in game_num :
		s3 = 0
		for i in range(0, 3) :
			if game3_numlist[i] in dice_numlist :
				s3 += 1
		if s3 >=2 : #2개 이상 맞았니?
			result3 = "You Win"
		else :
			result3 = "You Lose"
	else :
		result3 = '참여 X'

	return result3

def taisai_any_triple_game(game4_numlist, dice_numlist): #내가 선택한 주사위와 랜덤 주사위 배열 입력
	if 4 in game_num :
		s4 = 0
		for i in range(0, 3) :
			if game4_numlist[i] in dice_numlist :
				s4 += 1
		if s4 == 3 :
			result4 = "You Win"
		else :
			result4 = "You Lose"
	else :
		result4 = '참여 X'

	return result4

def taisai_triple_game(game5_numlist, dice_numlist):
	if 5 in game_num :
		if dice_numlist[0] == dice_numlist[1] and dice_numlist[1] == dice_numlist[2] :
			if game5_numlist[0] in dice_numlist :
				result5 = 'You Win'
			else :
				result5 = 'You Lose'
		else :
			result5 = 'You Lose'
	else :
		result5 = '참여 X'

	return result5

def taisai_single_dice_game():
	if 6 in game_num :
		if dice_numlist[0] == dice_numlist[1] and dice_numlist[1] == dice_numlist[2] :
			result6 = 'You Win'
		else :
			result6 = 'You Lose'
	else :
		result6 = '참여 X'

	return result6

def taisai_hard_number_game(game7_numlist, dice_numlist):
	if 7 in game_num :
		s7 = 0
		for i in range(0, 3):
			if game7_numlist[i] == dice_numlist[i] :
				s7 += 1
		if s7 == 3 :
			result7 = 'You Win'
		else :
			result7 = 'You Lose'
	else :
		result7 = '참여 X'

	return result7

def taisai_chip_cal():
	if result1 == "You Win":
		chip += game1_chip * 2
	if result2 == "You Win":
		chip += game2_chip * 2
	if result3 == "You Win":
		chip += game3_chip * 2
	if result4 == "You Win":
		chip += game4_chip * 2
	if result5 == "You Win":
		chip += game5_chip * 2
	if result6 == "You Win":
		chip += game6_chip * 2
	if result7 == "You Win":
		chip += game7_chip * 2

#---------------------------------------------

#폰트-------------------------------------------------------

font = pygame.font.SysFont("맑은 고딕", 60)


while True:
	clock.tick(50)

	how_many_chips = font.render("Chip : ", True, (0, 0, 0))


	#종료 관련-----------------------------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit() # X누르면 종료

	if bg_name == "bg_gameover":
		if quit_button.draw():
			sys.exit()

	#taisai_error_exception

	if bg_name == "bg_wrong":
		if back_button.draw():
			screen.blit(bg_main, (0, 0))
			bg_name = "bg_main"
			taisai_del()

	# bg_main에서의 버튼들----------------------------

	if bg_name == "bg_main":
		if start_button.draw():
			screen.blit(bg_game_choice, (0, 0))
			bg_name = "bg_game_choice"

	if bg_name == "bg_main":
		if credit_button.draw():
			screen.blit(bg_credit, (0, 0))
			bg_name = "bg_credit"

	# bg_credit에서의 버튼들-----------------------

	if bg_name == "bg_credit":
		if ok_button.draw():
			screen.blit(bg_main, (0, 0))
			bg_name = "bg_main"
		
	# bg_game_choice에서의 버튼들----------------------------

	if bg_name == "bg_game_choice":
		if back_button.draw():
			screen.blit(bg_main, (0, 0))
			bg_name = "bg_main"
	
	if bg_name == "bg_game_choice":
		if choice_slotgame_button.draw():
			screen.blit(bg_gamerule_slotgame, (0, 0))
			bg_name = "bg_gamerule_slotgame"

	if bg_name == "bg_game_choice":
		if choice_blackjack_button.draw():
			screen.blit(bg_gamerule_blackjack, (0, 0))
			bg_name = "bg_gamerule_blackjack"

	if bg_name == "bg_game_choice":
		if choice_poker_button.draw():
			screen.blit(bg_gamerule_poker, (0, 0))
			bg_name = "bg_gamerule_poker"

	if bg_name == "bg_game_choice":
		if choice_taisai_button.draw():
			screen.blit(bg_gamerule_taisai, (0, 0))
			bg_name = "bg_gamerule_taisai"

	# bg_gamerule_slotgame에서의 버튼들----------------------------

	if bg_name == "bg_gamerule_slotgame":
		if ok_button.draw():
			screen.blit(bg_slotgame, (0, 0))
			bg_name = "bg_slotgame"

	# bg_gamerule_blackjack에서의 버튼들----------------------------


	if bg_name == "bg_gamerule_blackjack":
		if ok_button.draw():
			screen.blit(bg_blackjack, (0, 0))
			bg_name = "bg_blackjack"

	# bg_gamerule_poker에서의 버튼들----------------------------

	if bg_name == "bg_gamerule_poker":
		if ok_button.draw():
			screen.blit(bg_gamerule_poker_2, (0, 0))
			bg_name = "bg_gamerule_poker_2"

	if bg_name == "bg_gamerule_poker_2":
		if ok_button.draw():
			screen.blit(bg_poker, (0, 0))
			bg_name = "bg_poker"

	# bg_gamerule_taisai에서의 버튼들----------------------------

	if bg_name == "bg_gamerule_taisai":
		if ok_button.draw():
			screen.blit(bg_taisai, (0, 0))
			bg_name = "bg_taisai"

	#bg_slotgame에서의 버튼들----------------------------

	if bg_name == "bg_slotgame":
		screen.blit(how_many_chips, (20, 20))
		screen.blit(chip_count, (590, 330)) # 66, 333이었음
		text_chip = font.render(str(chip), True, (0, 0, 0))
		text_input_chip = font.render(str(input_chip), False, (0, 0, 0))
		screen.blit(text_chip, (155, 23))
		screen.blit(text_input_chip, (714, 344)) #190, 347
		pygame.display.update()
		#repeat = False
		
	
	if bg_name == "bg_slotgame":
		if back_button.draw():
			screen.blit(bg_game_choice, (0, 0))
			bg_name = "bg_game_choice"
			repeat = True
			clear_chip()


	if bg_name == "bg_slotgame": #코인 up
		if state == 'S':
			if chip >= 0 and input_chip != chip:
				if chip_up_button.draw():
					input_chip += 1
					text_input_chip = font.render(str(input_chip), True, (255, 255, 255))
					screen.blit(bg_slotgame, (0, 0))
	"""
	if bg_name == "bg_slotgame": #코인 10up
		if state == 'S':
			if chip >= 0 and input_chip != chip:
				if chip_10up_button.draw():
					print("up")
					if (input_chip + 10) < chip:
						input_chip += 10
					elif (input_chip + 10) >= chip:
						input_chip = chip
					text_input_chip = font.render(str(input_chip), True, (255, 255, 255))
					screen.blit(bg_slotgame, (0, 0))
					#screen.blit(text_input_chip, (190, 347))
					print(chip, input_chip)
	"""

	if bg_name == "bg_slotgame": #코인 down
		if state == "S":
			if chip >= 1 and input_chip != 0:
				if chip_down_button.draw():
					if input_chip >= 1:
						input_chip -= 1
					elif input_chip < 0:
						input_chip = 0
					text_input_chip = font.render(str(input_chip), True, (255, 255, 255))
					screen.blit(bg_slotgame, (0, 0))
					pygame.display.update()
	"""
	if bg_name == "bg_slotgame": #코인 down
		if state == "S":
			if chip >= 1 and input_chip != 0:
				if chip_10down_button.draw():
					print("down")
					if input_chip >= 1:
						input_chip -= 10
						if input_chip < 0:
							input_chip = 0

					text_input_chip = font.render(str(input_chip), True, (255, 255, 255))
					screen.blit(bg_slotgame, (0, 0))
					#screen.blit(text_input_chip, (190, 347))
					print(chip, input_chip)
					pygame.display.update()
	"""

	if bg_name == "bg_slotgame":
		if state == "S":
			if input_chip >= 1 and chip != 0:
				if slotgame_start_button.draw():
					state == "F"
					screen.blit(bg_slotgame, (0, 0))
					pygame.display.update()
					result_list.append(slotgame(chip, input_chip))
					chip = result_list[0][0]
					result_list = []
					input_chip = 0
					text_chip = font.render(str(chip), True, (255, 255, 255))
					text_input_chip = font.render(str(input_chip), True, (255, 255, 255))
					screen.blit(bg_slotgame, (0, 0))
					if chip == 0:
						screen.blit(bg_gameover, (0, 0))
						bg_name = "bg_gameover"

	# bg_blackjack에서의 버튼들----------------------------
	
	if bg_name == "bg_blackjack":
		if back_button.draw():
			screen.blit(bg_game_choice, (0, 0))
			bg_name = "bg_game_choice"
			clear_chip()


	# bg_poker에서의 버튼들----------------------------

	if bg_name == "bg_poker":
		text_chip = font.render(str(chip), True, (0, 0, 0))
		text_input_chip = font.render(str(input_chip), False, (0, 0, 0))
		screen.blit(how_many_chips, (20, 20))
		screen.blit(chip_count, (900, 615))
		screen.blit(text_chip, (155, 23))
		screen.blit(text_input_chip, (1020, 625)) #190, 347
		pygame.display.update()

	if bg_name == "bg_poker": #코인 up
			if chip >= 0 and input_chip != chip:
				if po_chip_up_button.draw():
					input_chip += 1
					text_input_chip = font.render(str(input_chip), True, (255, 255, 255))
					screen.blit(bg_blackjack, (0, 0))

	if bg_name == "bg_poker": #코인 down
		if chip >= 1 and input_chip != 0:
			if po_chip_down_button.draw():
				if input_chip >= 1:
					input_chip -= 1
				elif input_chip < 0:
					input_chip = 0
				text_input_chip = font.render(str(input_chip), True, (255, 255, 255))
				screen.blit(bg_blackjack, (0, 0))
	
	if bg_name == "bg_poker":
		if back_button.draw():
			screen.blit(bg_game_choice, (0, 0))
			bg_name = "bg_game_choice"
			clear_chip()

	if bg_name == "bg_poker":
		if back_button.draw():
			screen.blit(bg_game_choice, (0, 0))
			bg_name = "bg_game_choice"
			repeat = True

	if bg_name == "bg_poker":
		poker()

	# bg_taisai에서의 버튼들----------------------------

	if bg_name == "bg_taisai":
		screen.blit(how_many_chips, (1040, 375))
		#screen.blit(chip_count, (590, 330)) # 66, 333이었음

		text_chip = font.render(str(chip), True, (0, 0, 0))
		text_game1_chip = font.render(str(game1_chip), False, (0, 0, 0))
		text_game2_chip = font.render(str(game2_chip), False, (0, 0, 0))
		text_game3_chip = font.render(str(game3_chip), False, (0, 0, 0))
		text_game4_chip = font.render(str(game4_chip), False, (0, 0, 0))
		text_game5_chip = font.render(str(game5_chip), False, (0, 0, 0))
		text_game6_chip = font.render(str(game6_chip), False, (0, 0, 0))
		text_game7_chip = font.render(str(game7_chip), False, (0, 0, 0))

		screen.blit(text_chip, (1175, 375))

		pygame.display.update()

	if bg_name == "bg_taisai":
		if taisai_back_button.draw():
			taisai_del()
			screen.blit(bg_game_choice, (0, 0))
			bg_name = "bg_game_choice"
			clear_chip()

	if bg_name == "bg_taisai":
		if game1_chip != 0 or game2_chip != 0 or game3_chip != 0 or game4_chip != 0 or game5_chip != 0 or game6_chip != 0 or game7_chip != 0:
			if taisai_start_button.draw():

				numlist1 = len(game1_numlist)
				numlist2 = len(game2_numlist)
				numlist3 = len(game3_numlist)
				numlist4 = len(game4_numlist)
				numlist5 = len(game5_numlist)
				numlist7 = len(game7_numlist)
				if game_num.count(1) > 0:
					if len(game1_numlist) < 1:
						screen.blit(bg_wrong, (0, 0))
						bg_name = "bg_wrong"
				if game_num.count(2) > 0:
					if len(game2_numlist) < 1:
						screen.blit(bg_wrong, (0, 0))
						bg_name = "bg_wrong"
				if game_num.count(3) > 0:
					if len(game3_numlist) < 3:
						screen.blit(bg_wrong, (0, 0))
						bg_name = "bg_wrong"
				if game_num.count(4) > 0:
					if len(game4_numlist) < 3:
						screen.blit(bg_wrong, (0, 0))
						bg_name = "bg_wrong"
				if game_num.count(6) > 0:
					if len(game5_numlist) < 1:
						screen.blit(bg_wrong, (0, 0))
						bg_name = "bg_wrong"
				if game_num.count(7) > 0:
					if len(game7_numlist) < 3:
						screen.blit(bg_wrong, (0, 0))
						bg_name = "bg_wrong"
					
				if bg_name != "bg_wrong":
					taisai = taisai_dice_selection()
					dice_numlist =taisai[0]
					sum_dice = taisai[1]
					result1 = taisai_big_small_game(sum_dice)
					result2 = taisai_even_odd_game(sum_dice)
					result3 = taisai_pair_dice_game(game3_numlist, dice_numlist)
					result4 = taisai_any_triple_game(game4_numlist, dice_numlist)
					result5 = taisai_triple_game(game5_numlist, dice_numlist)
					result6 = taisai_single_dice_game()
					result7 = taisai_hard_number_game(game7_numlist, dice_numlist)
					screen.blit(bg_taisai_result, (0, 0))
					bg_name = "bg_taisai_result"
					if result1 == "You Win":
						chip += game1_chip * 2
						screen.blit(result_win_img, (21, 10))
					elif result1 == 'You Lose' :
						screen.blit(result_lose_img, (21, 10))
					else :
						screen.blit(result_x_img, (21, 10))

					if result2 == "You Win":
						chip += game2_chip * 2
						screen.blit(result_win_img, (363, 10))
					elif result2 == 'You Lose' :
						screen.blit(result_lose_img, (363, 10))
					else :
						screen.blit(result_x_img, (363, 10))

					if result3 == "You Win":
						chip += game3_chip * 2
						screen.blit(result_win_img, (705, 10))
					elif result3 == 'You Lose' :
						screen.blit(result_lose_img, (705, 10))
					else :
						screen.blit(result_x_img, (705, 10))

					if result4 == "You Win":
						chip += game4_chip * 2
						screen.blit(result_win_img, (1047, 10))
					elif result4 == 'You Lose' :
						screen.blit(result_lose_img, (1047, 10))
					else :
						screen.blit(result_x_img, (1047, 10))

					if result5 == "You Win":
						chip += game5_chip * 2
						screen.blit(result_win_img, (21, 370))
					elif result5 == 'You Lose' :
						screen.blit(result_lose_img, (21, 370))
					else :
						screen.blit(result_x_img, (21, 370))

					if result6 == "You Win":
						chip += game6_chip * 2
						screen.blit(result_win_img, (363, 370))
					elif result6 == 'You Lose' :
						screen.blit(result_lose_img, (363, 370))
					else :
						screen.blit(result_x_img, (363, 370))

					if result7 == "You Win":
						chip += game7_chip * 2
						screen.blit(result_win_img, (705, 370))
					elif result7 == 'You Lose' :
						screen.blit(result_lose_img, (705, 370))
					else :
						screen.blit(result_x_img, (705, 370))
			
				pygame.display.update()
			

	#베팅 선택에서 버튼들#
	if bg_name == 'bg_taisai':
		if big_small_button.draw():
			big_small_select_button.draw()
			pygame.display.update()
			pygame.time.delay(300)
			game_num.append(1)
		if even_odd_button.draw():
			even_odd_select_button.draw()
			pygame.display.update()
			pygame.time.delay(300)
			game_num.append(2)
		if pair_dice_button.draw():
			pair_dice_select_button.draw()
			pygame.display.update()
			pygame.time.delay(300)
			game_num.append(3)
		if any_triple_button.draw():
			any_triple_select_button.draw()
			pygame.display.update()
			pygame.time.delay(300)
			game_num.append(4)
		if triple_button.draw():
			triple_select_button.draw()
			pygame.display.update()
			pygame.time.delay(300)
			game_num.append(5)
		if single_dice_button.draw():
			single_dice_select_button.draw()
			pygame.display.update()
			pygame.time.delay(300)
			game_num.append(6)
		if hard_number_button.draw():
			hard_number_select_button.draw()
			pygame.display.update()
			pygame.time.delay(300)
			game_num.append(7)
		
		#game 1
		
		if game_num.count(1) > 0:
			if big_button.draw():
				big_select_button.draw()
				game1_numlist.append(1)
				pygame.display.update()
				pygame.time.delay(500)
			if small_button.draw():
				small_select_button.draw()
				game1_numlist.append(2)
				pygame.display.update()
				pygame.time.delay(500)

		#gmae 2
		if game_num.count(2) > 0:
			if even_button.draw():
				even_select_button.draw()
				game2_numlist.append(1)
				pygame.display.update()
				pygame.time.delay(500)
			if odd_button.draw():
				odd_select_button.draw()
				game2_numlist.append(2)
				pygame.time.delay(500)
				pygame.display.update()

		#game 3
		if game_num.count(3) > 0:
			if len(game3_numlist) < 3:
				if game3_dicenum1_button.draw():
					game3_numlist.append(1)
					game3_dicenum1_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game3_dicenum2_button.draw():
					game3_numlist.append(2)
					game3_dicenum2_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game3_dicenum3_button.draw():
					game3_numlist.append(3)
					game3_dicenum3_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game3_dicenum4_button.draw():
					game3_numlist.append(4)
					game3_dicenum4_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game3_dicenum5_button.draw():
					game3_numlist.append(5)
					game3_dicenum5_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game3_dicenum6_button.draw():
					game3_numlist.append(6)
					game3_dicenum6_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
			else:
				game3_dicenum1_button.draw()
				game3_dicenum2_button.draw()
				game3_dicenum3_button.draw()
				game3_dicenum4_button.draw()
				game3_dicenum5_button.draw()
				game3_dicenum6_button.draw()

		#game 4
		if game_num.count(4) > 0:
			if len(game4_numlist) < 3:
				if game4_dicenum1_button.draw():
					game4_numlist.append(1)
					game4_dicenum1_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game4_dicenum2_button.draw():
					game4_numlist.append(2)
					game4_dicenum2_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game4_dicenum3_button.draw():
					game4_numlist.append(3)
					game4_dicenum3_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game4_dicenum4_button.draw():
					game4_numlist.append(4)
					game4_dicenum4_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game4_dicenum5_button.draw():
					game4_numlist.append(5)
					game4_dicenum5_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game4_dicenum6_button.draw():
					game4_numlist.append(6)
					game4_dicenum6_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
			else:
				game4_dicenum1_button.draw()
				game4_dicenum2_button.draw()
				game4_dicenum3_button.draw()
				game4_dicenum4_button.draw()
				game4_dicenum5_button.draw()
				game4_dicenum6_button.draw()

		#game 5
		if game_num.count(5) > 0:
			if len(game5_numlist) < 3:
				if game5_dicenum1_button.draw():
					game5_numlist.append(1)
					game5_dicenum1_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game5_dicenum2_button.draw():
					game5_numlist.append(2)
					game5_dicenum2_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game5_dicenum3_button.draw():
					game5_numlist.append(3)
					game5_dicenum3_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game5_dicenum4_button.draw():
					game5_numlist.append(4)
					game5_dicenum4_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game5_dicenum5_button.draw():
					game5_numlist.append(5)
					game5_dicenum5_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game5_dicenum6_button.draw():
					game5_numlist.append(6)
					game5_dicenum6_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
			else:
				game5_dicenum1_button.draw()
				game5_dicenum2_button.draw()
				game5_dicenum3_button.draw()
				game5_dicenum4_button.draw()
				game5_dicenum5_button.draw()
				game5_dicenum6_button.draw()

		#game 6

		#game 7
		if game_num.count(7) > 0:
			if len(game7_numlist) < 3:
				if game7_dicenum1_button.draw():
					game7_numlist.append(1)
					game7_dicenum1_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game7_dicenum2_button.draw():
					game7_numlist.append(2)
					game7_dicenum2_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game7_dicenum3_button.draw():
					game7_numlist.append(3)
					game7_dicenum3_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game7_dicenum4_button.draw():
					game7_numlist.append(4)
					game7_dicenum4_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game7_dicenum5_button.draw():
					game7_numlist.append(5)
					game7_dicenum5_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
				if game7_dicenum6_button.draw():
					game7_numlist.append(6)
					game7_dicenum6_select_button.draw()
					pygame.display.update()
					pygame.time.delay(500)
			else:
				game7_dicenum1_button.draw()
				game7_dicenum2_button.draw()
				game7_dicenum3_button.draw()
				game7_dicenum4_button.draw()
				game7_dicenum5_button.draw()
				game7_dicenum6_button.draw()

	#배팅 버튼

		#game1 배팅
		taisai_chip = game1_chip + game2_chip + game3_chip + game4_chip + game5_chip + game6_chip + game7_chip
		if chip >= 0:
			if len(game1_numlist) > 0:
				screen.blit(text_game1_chip, (230, 140))
				if chip > 0:
					if chip_up_button1.draw():
						screen.blit(bg_taisai, (0, 0))
						game1_chip += 1
						chip -= 1
			if len(game2_numlist) > 0:
				screen.blit(text_game2_chip, (570, 140))
				if chip > 0:
					if chip_up_button2.draw():
						screen.blit(bg_taisai, (0, 0))
						game2_chip += 1
						chip -= 1
			if len(game3_numlist) > 0:
				screen.blit(text_game3_chip, (910, 140))
				if chip > 0:
					if chip_up_button3.draw():
						screen.blit(bg_taisai, (0, 0))
						game3_chip += 1
						chip -= 1
			if len(game4_numlist) > 0:
				screen.blit(text_game4_chip, (1250, 140))
				if chip > 0:
					if chip_up_button4.draw():
						screen.blit(bg_taisai, (0, 0))
						game4_chip += 1
						chip -= 1
			if len(game5_numlist) > 0:
				screen.blit(text_game5_chip, (230, 505))
				if chip > 0:
					if chip_up_button5.draw():
						screen.blit(bg_taisai, (0, 0))
						game5_chip += 1
						chip -= 1
			if game_num.count(6) > 0:
				screen.blit(text_game6_chip, (570, 505))
				if chip > 0:
					if chip_up_button6.draw():
						screen.blit(bg_taisai, (0, 0))
						game6_chip += 1
						chip -= 1
			if len(game7_numlist) > 0:
				screen.blit(text_game7_chip, (910, 505))
				if chip > 0:
					if chip_up_button7.draw():
						screen.blit(bg_taisai, (0, 0))
						game7_chip += 1
						chip -= 1
		if taisai_chip > 0:
			if len(game1_numlist) > 0:
				if chip_down_button1.draw():
					screen.blit(bg_taisai, (0, 0))
					game1_chip -= 1
					chip += 1
			if len(game2_numlist) > 0:		
				if chip_down_button2.draw():
					screen.blit(bg_taisai, (0, 0))
					game2_chip -= 1
					chip += 1
			if len(game3_numlist) > 0:
				if chip_down_button3.draw():
					screen.blit(bg_taisai, (0, 0))
					game3_chip -= 1
					chip += 1
			if len(game4_numlist) > 0:
				if chip_down_button4.draw():
					screen.blit(bg_taisai, (0, 0))
					game4_chip -= 1
					chip += 1
			if len(game5_numlist) > 0:
				if chip_down_button5.draw():
					screen.blit(bg_taisai, (0, 0))
					game5_chip -= 1
					chip += 1
			if game_num.count(6) > 0:
				if chip_down_button6.draw():
					screen.blit(bg_taisai, (0, 0))
					game6_chip -= 1
					chip += 1
			if len(game7_numlist) > 0:
				if chip_down_button7.draw():
					screen.blit(bg_taisai, (0, 0))
					game7_chip -= 1
					chip += 1


	if bg_name == "bg_taisai_result":   #결과창으로 이동

		if dice_numlist[0] == 1:
			screen.blit(result_dice1_img, (1037, 450))
		elif dice_numlist[0] == 2:
			screen.blit(result_dice2_img, (1037, 450))
		elif dice_numlist[0] == 3 :
			screen.blit(result_dice3_img, (1037, 450))
		elif dice_numlist[0] == 4 :
			screen.blit(result_dice4_img, (1037, 450))
		elif dice_numlist[0] == 5 :
			screen.blit(result_dice5_img, (1037, 450))
		elif dice_numlist[0] == 6 :
			screen.blit(result_dice6_img, (1037, 450))

		if dice_numlist[1] == 1 :
			screen.blit(result_dice1_img, (1147, 450))
		elif dice_numlist[1] == 2 :
			screen.blit(result_dice2_img, (1147, 450))
		elif dice_numlist[1] == 3 :
			screen.blit(result_dice3_img, (1147, 450))
		elif dice_numlist[1] == 4 :
			screen.blit(result_dice4_img, (1147, 450))
		elif dice_numlist[1] == 5 :
			screen.blit(result_dice5_img, (1147, 450))
		elif dice_numlist[1] == 6 :
			screen.blit(result_dice6_img, (1147, 450))

		if dice_numlist[2] == 1 :
			screen.blit(result_dice1_img, (1257, 450))
		elif dice_numlist[2] == 2 :
			screen.blit(result_dice2_img, (1257, 450))
		elif dice_numlist[2] == 3 :
			screen.blit(result_dice3_img, (1257, 450))
		elif dice_numlist[2] == 4 :
			screen.blit(result_dice4_img, (1257, 450))
		elif dice_numlist[2] == 5 :
			screen.blit(result_dice5_img, (1257, 450))
		elif dice_numlist[2] == 6:
			screen.blit(result_dice6_img, (1257, 450))
		bg_name = 'bg_taisai_result'

	if bg_name == 'bg_taisai_result':
		if taisai_back_button.draw():
			taisai_del()
			game1_chip = 0
			game2_chip = 0
			game3_chip = 0
			game4_chip = 0
			game5_chip = 0
			game6_chip = 0
			game7_chip = 0

			screen.blit(bg_taisai, (0, 0))
			text_game1_chip = font.render(str(game1_chip), False, (0, 0, 0))
			text_game2_chip = font.render(str(game2_chip), False, (0, 0, 0))
			text_game3_chip = font.render(str(game3_chip), False, (0, 0, 0))
			text_game4_chip = font.render(str(game4_chip), False, (0, 0, 0))
			text_game5_chip = font.render(str(game5_chip), False, (0, 0, 0))
			text_game6_chip = font.render(str(game6_chip), False, (0, 0, 0))
			text_game7_chip = font.render(str(game7_chip), False, (0, 0, 0))

			if chip == 0:
				screen.blit(bg_gameover, (0, 0))
				bg_name = "bg_gameover"
			else:
				bg_name = 'bg_taisai'

	# bg_blackjack에서의 버튼들--------------------------------------------------------
	if bg_name == "bg_blackjack":
		text_chip = font.render(str(chip), True, (0, 0, 0))
		text_input_chip = font.render(str(input_chip), False, (0, 0, 0))
		if blackjack_state != "start":
			screen.blit(how_many_chips, (20, 20))
			screen.blit(chip_count, (900, 615))
			screen.blit(text_chip, (155, 23))
			screen.blit(text_input_chip, (1020, 625)) #190, 347
		pygame.display.update()

	if bg_name == "bg_blackjack": #코인 up
		if blackjack_state != 'start':
			if chip >= 0 and input_chip != chip:
				if bj_chip_up_button.draw():
					input_chip += 1
					text_input_chip = font.render(str(input_chip), True, (255, 255, 255))
					screen.blit(bg_blackjack, (0, 0))

	if bg_name == "bg_blackjack": #코인 down
		if blackjack_state != 'start':
			if chip >= 1 and input_chip != 0:
				if bj_chip_down_button.draw():
					if input_chip >= 1:
						input_chip -= 1
					elif input_chip < 0:
						input_chip = 0
					text_input_chip = font.render(str(input_chip), True, (255, 255, 255))
					screen.blit(bg_blackjack, (0, 0))

	if bg_name == "bg_blackjack":
		if blackjack_state != "start":
			if input_chip > 0:
				if bj_start_button.draw():
					screen.blit(bg_blackjack, (0, 0))
					chip = chip - input_chip
					blackjack()
					pygame.display.update()
					blackjack_state = "start"

	if bg_name == "bg_blackjack":
		if blackjack_state == "start":
			if bj_stay_button.draw():
				reward = choose_stay()
				chip = chip + input_chip * int(reward)
				input_chip = 0
				screen.blit(bg_blackjack, (0, 0))
				if chip == 0:
					screen.blit(bg_gameover, (0, 0))
					bg_name = "bg_gameover"
				pygame.display.update()

	if bg_name == "bg_blackjack":
		if blackjack_state == "start":
			if total(playerhand) < 21:       
				if bj_hit_button.draw():
					reward = choose_hit()
					if chip_state == "clear":
						chip = chip + input_chip * int(reward)
						input_chip = 0
						screen.blit(bg_blackjack, (0, 0))
						chip_state = " "
						if chip == 0:
							screen.blit(bg_gameover, (0, 0))
							bg_name = "bg_gameover"
					pygame.display.update()



	pygame.display.update() # 화면을 계속 업데이트해주는 함수