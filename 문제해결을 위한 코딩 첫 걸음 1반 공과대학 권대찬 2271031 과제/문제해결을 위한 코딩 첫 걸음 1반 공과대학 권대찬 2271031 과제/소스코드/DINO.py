#학번: 2271031
#이름: 권대찬
#내용: 크롬 공룡게임과 유사한 공룡이 장애물들을 넘어가며 점수를 얻는 게임

import pygame #파이게임 라이브러리 불러오기
import random #밑에 사용할 새의 무작위 출현을 위한 난수 라이브러리
import sys #시스템 모듈 넣기 X를 누르면 종료되도록
from tkinter import * #메뉴에 사용할 tkinter 라이브러리
pygame.init()  #키보드, 사운드 처럼 게임에 사용할 하드웨어 요소를 위해 초기화하는 역할
pygame.mixer.init() #믹서 모듈 초기화, 음악, 소리를 넣기 위한 함수                                                                                         


def game_start_button(): #메뉴에서 게임 시작 버튼 함수
    btn_gamestart = Button(root, text = "게임 시작!",fg= "white",bg="limegreen", #배경 라임그린, 글꼴색 흰색 버튼
    width= 15,height = 2,font = "Hack",relief = "groove",command = game_start) #'Hack' 폰트와 'Groove' 테두리 스타일의 버튼, 버튼 클릭 시 게임이 시작됨
    btn_gamestart.pack() #공룡 캐릭터 이미지 밑에 배치되도록 함

def creator(): #하단 좌측에 게임을 개발한 사람의 문구 함수
    lbl_creator = Label(root, text = "제작자: 2271031 권대찬",bg= "sienna",fg="lightsalmon") #황토색 글꼴 배경과 연분홍색 글꼴색의 개발자 레이블
    lbl_creator.place(x=1,y=380)  #x축 1, y축 380에 배치함

def menu_music(): #게임 시작 전 메뉴에 나오는 음악을 저장하고 있는 함수
    pygame.mixer.music.load(music_list['menu']) #위에서 초기화된 mixer.init()을 이용하여 음악을 로드 할 수 있도록함. 음악리스트 딕셔너리에서 'menu'키를 불러와서 노래를 출력                                      
    pygame.mixer.music.play()  #음악을 재생시켜줌
    btn_music = Button(root, image = music_Image, height = 100, width = 100,command = music_button_command,bg="limegreen") 
    #음악 버튼을 클릭하게 되면 밑에 music_button_command가 불러와지고 음소거 된다                                                                                                                               
    btn_music.place(x=495 ,y=295) #음악 버튼은 우측 하단에 위치하도록 배치

def music_button_command(): #음악 버튼을 클릭할 경우 음소거 이미지가 출력됨과 동시에 음악도 멈추게 되는 함수
    pygame.mixer.music.stop() #음악을 멈추게 함
    btn_mute = Button(root, image = mute_Image,height = 100, width = 100,command = restart_music_command,bg="limegreen") 
    #음소거 이미지를 불러오고 클릭시 밑에 음악재시작 함수인 restart_music_command를 불러오고 음악 다시 시작
    btn_mute.place(x=495, y= 295) #음악 버튼과 마찬가지로 음소거 버튼또한 같은 우측 하단에 배치

def restart_music_command(): #음소거 버튼을 클릭했을 경우 다시 음악 이미지와 버튼을 불러와서 음악을 재시작하는 함수
    pygame.mixer.music.load(music_list['menu']) #음악 불러옴
    pygame.mixer.music.play()  #음악을 재생시켜줌
    btn_music = Button(root, image = music_Image, height = 100, width = 100,command = music_button_command,bg="limegreen") #재시작 버튼
    btn_music.place(x=495,y=295) #음악 재시작 버튼 배치
    #위에서 말한 menu_music(): 함수를 이름만 다르게 했을 뿐 형식은 비슷하다
  
def game_introduce(): #게임시작 버튼 밑에 배치된 게임 설명서 버튼 클릭시 나오는 설명서 함수이다.
    global game_introducer #설명서 클릭시 사라지도록 하기 위해 존재하는 함수에서도 호출할 수 있도록 전역변수로 사용 
    game_introducer = Button(root, text = """1. 방향키 ⇧를 눌러서 점프 \n2. 달릴때마다 점수가 올라갑니다 \n3. 장애물에 닿으면 죽습니다 \n4. 점수가 증가할수록 게임속도가 빨라집니다
    5. 400점 때 새가 출몰합니다 \n6. 1000점, 1500점부터 어려워집니다.""",font = "Hack",relief = "groove",command = game_introduce_hide)
    #설명서 내용또한 버튼 형식으로 클릭시 game_introduce_hide() 이벤트를 불러온다. 클릭시 내용이 사라지게 된다.
    game_introducer.place(x = 50, y = 190) #게임설명서 버튼 위에 중첩되어 배치되도록 거의 동일한 위치에 배치

def game_introduce_hide(): #버튼 클릭시 설명서 내용이 사라지고 게임설명서 버튼이 뜨게 하는 함수
    game_introducer.place_forget() #place_forget()을 이용하 place로 배치된 설명서 내용이 지워지도록 함

def game_start(): #게임이 동작되는 함수, 이미지와 게임 방식 참조: https://blockdmask.tistory.com/419 [개발자 지망생:티스토리]
    global points,jump_top, x_pos_bg, y_pos_bg, bird_x, bird_y,tree_x,cloud_x,dino_y #함수 사이, 함수 밖에서 주로 사용될 것들을 전역 변수로 정의
    pygame.display.set_caption('게임화면') #파이게임의 제목 설정
    pygame.mixer.music.load(music_list['game']) #'game'를 호출하고 게임시작 시 음악을 다른 것으로 바꿈                                                             
    pygame.mixer.music.play() #음악 재생
    BG = pygame.image.load("track.png") #게임에서 캐릭터가 달리는 트랙 이미지를 불러옴
    x_pos_bg = 0 #트랙을 0으로 초기화
    y_pos_bg = 390 #390으로 트랙 초기화
    MAX_WIDTH = 800 #게임화면의 너비를 800으로 지정
    MAX_HEIGHT = 400 #게임화면의 높이를 400으로 지정
    root.withdraw() #메뉴가 사라지고 게임 화면만 나오게 함
    points = 0 #점수를 0점으로 초기화
    def background(): #캐릭터가 달릴 트랙 함수
        global x_pos_bg, y_pos_bg #함수 밖에서의 전역 변수 사용을 위해 재정의
        image_width = BG.get_width() #가로 x축의 방향 길이를 저장
        screen.blit(BG, (x_pos_bg, y_pos_bg)) #위에서 정의된 0, 390가 저장된 함수에 맞게 배경 이미지 배치
        screen.blit(BG, (image_width + x_pos_bg, y_pos_bg)) #얻어낸 가로 x축의 길이를 더하여 화면에 맞게 배치
        
    def score(): #게임 점수 함수, https://www.youtube.com/watch?v=KbKMqxVw8x0 참조
        global points, bird_x, bird_y,tree_x,cloud_x,dino_y,jump_top #전역 변수 재정의
        points += 1 #점수가 1씩 증가
        font = pygame.font.SysFont("FixedSsy", 30, 1, 0) #점수의 폰트를 FixedSsy로 설정
        text = font.render("Points: "+ str(points), 1, (0, 0, 0)) #Points: 에 누적되는 points를 더하여 출력
        textRect = text.get_rect() #텍스트의 좌표 저장
        textRect.center = (700, 30) #좌표값을 입력
        screen.blit(text, textRect) #점수 텍스트를 넣기
        if points >= 400: #400이상일 경우 템포가 빨라짐
            bird_x -= random.randint(25.0,45.0) #25.0과 45.0 사이의 난수가 발생하며 속도가 빨라짐
            if bird_x <= 0: #새의 x좌표가 0이하일 경우
                bird_x = MAX_WIDTH #새의 x축은 최대 너비인 MAX_WIDTH의 값으로 이동
                bird_y = random.randint(10,675) #새의 y축 10~675 랜덤으로 출몰 
            screen.blit(imgBird, (bird_x, bird_y)) #새 이미지 넣기
            tree_x -= 5.0 #속도 5.0 추가로 증가
            cloud_x -= 5.0 #속도 5.0 추가로 증가
            jump_top = 110 # 공룡 jump 높이 증가
            if is_go_up:#공룡이 점프
                dino_y -= 10.0 #공룡이 점프하는 속도 증가
            elif not is_go_up and not is_bottom:#공룡이 점프에서 떨어지는 속도
                dino_y += 10.0 #떨어지는 속도 증가
        if points >= 1000: #1000점 이상일 경우 더 빨라짐
            bird_x -= random.randint(35.0,40.0) #새의 속도가 35.0 40.0 사이로 랜덤하게 속도 증가
            tree_x -= 7.0 #나무 속도 7.0 증가
            cloud_x -= 7.0 #구름 속도 7.0증가
            jump_top = 100 #점프 속도 더 증가
            if is_go_up: #공룡 점프했을 때
                dino_y -= 5.0 #빠르게 점프
            elif not is_go_up and not is_bottom: #떨어질 때
                dino_y += 5.0 #빠르게 떨어짐
        if points >= 1500: #1500점 이상일 경우 어려워짐
            bird_x -= random.randint(40.0,45.0) #새의 속도 매우 증가
            tree_x -= 7.0 # 나무 속도 매우 증가
            cloud_x -= 7.0 # 구름 속도 매우 증가
            jump_top = 90 #점프 속도 증가
            if is_go_up: #점프 하는 속도
                dino_y -= 5.0 #5.0 증가
            elif not is_go_up and not is_bottom: # 바닥으로 떨어지는 속도
                dino_y += 5.0 #5.0 증가
    def crash(): #충돌 처리 함수, https://blog.dalso.org/language/python/14188 참조
        global points #points 변수 재정의
        dino_rect = imgDino1.get_rect() #충돌 판정을 위한 공룡 이미지 좌표 얻기
        dino_rect.left = dino_x #충돌 처리를 위한 공룡 x좌표
        dino_rect.top = dino_y #충돌 처리를 위한 공룡 y좌표
        tree_rect = imgTree.get_rect() #충돌 판정을 위한 나무 장애물 좌표 얻기
        tree_rect.left = tree_x #나무의 충돌 판정 x좌표 
        tree_rect.top = tree_y #나무의 충돌 판정 y좌표 
        bird_rect =  imgBird.get_rect() #충돌 판정을 위한 새 이미지 좌표 얻기
        bird_rect.left = bird_x #충돌 판정을 위한 새의 x좌표
        bird_rect.top = bird_y #충돌 판정을 위한 새의 y좌표
        def rect(): #충돌 시 게임오버가 출력되는 함수 https://www.youtube.com/watch?v=xQ5UCzFKR58 부분 참조
            pygame.mixer.music.load(music_list['game_over']) #'game_over' 키로 호출하여 게임오버 노래 불러옴
            pygame.mixer.music.play() #음악 재생
            screen.fill((255, 255, 255)) #게임 화면을 RGB 값을 이용해 흰색 배경으로 적용
            font_gameover = pygame.font.SysFont("FixedSsy", 80, True, False) #게임오버 폰트 크기 80
            text_gameover = font_gameover.render('GAME OVER',False,(0,255,128)) #충돌 됐을 경우 GAME OVER 텍스트가 나옴
            textRect = text_gameover.get_rect() #텍스트의 좌표
            textRect.center = (400, 30) #텍스트의 x, y 좌표
            screen.blit(text_gameover,textRect) #텍스트 넣기

            font_points = pygame.font.SysFont("FixedSsy", 30, True, False) #게임하는 동안 얻은 점수의 폰트 크기 30
            text_points = font_points.render('Your score: '+str(points),False,(255,128,128)) #Your score에 총 얻은 점수를 더하여 출력
            textRect = text_points.get_rect() #텍스트의 좌표
            textRect.center = (400, 80) #텍스트 x,y 좌표
            screen.blit(text_points,textRect) #텍스트 삽입

            pygame.display.update() #pygame 디스플레이 업데이트
            pygame.time.delay(3000) #3초의 딜레이를 둠
            pygame.quit() #pygame을 종료함
            sys.exit() #시스템 모듈 종료
        if dino_rect.colliderect(tree_rect): #나무에 충돌했을 때 함수 호출
            rect() #충돌 함수 
        elif dino_rect.colliderect(bird_rect): #새에 충돌했을 경우에도 함수 호출
            rect()# 충돌 함수
        
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))#위에서 정의된 pygame 화면의 높이, 너비 설정
    fps = pygame.time.Clock() #게임 프레임 속도 제어
   
    imgDino1 = pygame.image.load('dino1.png') #공룡의 이미지를 불러옴
    imgDino2 = pygame.image.load('dino2.png') #공룡의 움직임을 주기 위해 다리가 전환된 이미지도 불러옴
    dino_height = imgDino1.get_size()[1] #공룡의 표면 치수를 얻음
    dino_bottom = MAX_HEIGHT - dino_height #공룡이 서있는 바닥 부분을 전체 높이에서 공룡의 치수 만큼 빼서 구함
    dino_x = 50 #공룡의 X좌표
    dino_y = dino_bottom #공룡의 Y좌표 바닥에 배치
    jump_top = 120 #공룡이 점프 높이를 조정
    leg_swap = True #공룡의 다리가 움직이므로 True
    is_bottom = True #공룡이 바닥에 있으므로 True
    is_go_up = False #공룡이 점프 중이 아니므로 False

    imgTree = pygame.image.load('tree.png') #나무 장애물 이미지를 불러옴
    tree_height = imgTree.get_size()[1] #나무의 표면 치수를 얻음
    tree_x = MAX_WIDTH #나무의 x좌표
    tree_y = MAX_HEIGHT - tree_height -5 #나무의 y좌표

    imgCloud = pygame.image.load('cloud.png') #배경 구름 이미지
    cloud_x = MAX_WIDTH #구름의 x좌표
    cloud_y = MAX_HEIGHT - 350 #구름의 y좌표

    imgBird = pygame.image.load("bird.gif") #새 장애물 이미지 불러오기
    bird_x = MAX_WIDTH #새의 x좌표
    bird_y = random.randint(10, 700)   #10에서 700까지 난수를 생성하여 새가 날아다니는 위치 조정
    while 1: #게임의 무한반복, 다리의 움직임, 장애물 등장 등등이 계속 진행되도록 while 사용
        screen.fill((255, 255, 255)) #화면 색은 하얗게
        for event in pygame.event.get(): #변수 event안에 pygame이 제공하는 event모음을 for문으로 반복해서 사용
            if event.type == pygame.QUIT: #창닫기 클릭시 사용되는 경우
                pygame.quit() #pygame이 종료됨
                sys.exit() #system 모듈 또한 종료됨
            elif event.type == pygame.KEYDOWN: #키보드를 누른 후 뗄 때 발생하는 경우
                if is_bottom: #바닥일 경우
                    is_go_up = True #바닥 상태가 False가 되어 go up 상태는 True가 된 후 공룡 점프
                    is_bottom = False #공룡의 바닥에 있는 상태가 False로 전환
      
        if is_go_up: #공룡이 위로 점프하는 경우
            dino_y -= 25.0 #위로 점프하는 속도
        elif not is_go_up and not is_bottom: #점프 상태도 아니고 바닥 상태도 아닌 공중 상태일 경우
            dino_y += 25.0 #바닥으로 착지하는 속도
        
        if is_go_up and dino_y <= jump_top: #점프가 지정된 y축의 경계일 경우
            is_go_up = False #점프가 활성화 되지 않음

        if not is_bottom and dino_y >= dino_bottom: #바닥이 아닌 상태가 아니고 공룡의 y축보다 크거나 같을 경우
            is_bottom = True #바닥 상태 True
            dino_y = dino_bottom #공룡의 y축은 바닥

        tree_x -= random.randint(13.0, 24.0) #나무가 x축으로 공룡에게 다가오는 속도가 13.0, 24.0 사이에서 랜덤으로 적용됨
        if tree_x <= 0: #만약 x축이 0보다 작아지면
            tree_x = MAX_WIDTH #x축의 처음 자리인 MAX_WIDTH로 이동
        
        cloud_x -= 10.0 #구름이 좌측 x측 끝으로 다가오는 속도
        if cloud_x <= 0: #구름이 너비를 넘어가면
            cloud_x = MAX_WIDTH #다시 처음인 우측으로
           
        screen.blit(imgCloud, (cloud_x, cloud_y)) #구름 이미지 배치
        screen.blit(imgTree, (tree_x, tree_y)) #나무 이미지 배치

        if leg_swap: #다리의 움직임
            screen.blit(imgDino1, (dino_x, dino_y))#스크린에 공룡 그림 1출력
            leg_swap = False #다리의 움직임 0
        else: #다리의 다른 움직임
            screen.blit(imgDino2, (dino_x, dino_y)) #스크린에 공룡 그림 2출력
            leg_swap = True #다리의 움직임 1
        background() #배경함수 호출
        score() #점수 함수 호출
        crash() #충돌처리 함수 호출
        
        pygame.display.flip() #화면 전체를 업데이트함
        pygame.display.update() #파이게임 디스플레이 업데이트
        fps.tick(30) #시계 업데이트 프레임
    
root = Tk() #tkinter를 root로 선언
root.title("공룡게임") #제목을 공룡게임으로 정의
root.geometry("600x400") #게임 메뉴화면의 크기를 600x400으로 정의
wall = PhotoImage(file = "./batang.png") #메뉴의 배경화면 이미지를 불러옴
wall_label = Label(image = wall) #wall에서 불러온 이미지를 레이블로 선언
wall_label.place(x = 1,y = 1) #배경이 꽉차게 배치함

menu_Image = PhotoImage(file = "./DINO_MENU.png") #메뉴에 상단에 있는 공룡 이미지를 불러옴
lbl_menu_Image = Label(root,image = menu_Image) #공룡 이미지 레이블로 선언
lbl_menu_Image.pack() #최상단에 배치

music_Image = PhotoImage(file = "./Music.png") #음악 이미지
mute_Image = PhotoImage(file = "./Musicoff.png") #음소거 이밎
music_list = { } #음악 리스트 딕셔너리
music_list['menu'] = "MENU THEME.mp3" #키 'menu'를 호출하여 메뉴에 나오는 음악을 출력
music_list['game'] = "Game Music.mp3" #키 'game'을 호출하여 게임 시작시 등장하는 음악 출력
music_list['game_over'] = "Game Over.mp3" #키 'game_over'를 호출하여 게임에서 캐릭터가 충돌 시 나오는 노래 출력

menu_music() #메뉴 음악 함수 호출
game_start_button() #게임 시작 버튼 함수 호출
creator() #게임 제작자 레이블 함수 호출
btn_introduce = Button(root, text = "게임 설명서",fg= "white",bg="limegreen",
width= 15,height = 2,font = "Hack",relief = "groove",command = game_introduce) #게임 설명서 버튼으로 클릭시 설명서 내용 버튼이 출력됨 
btn_introduce.pack() #게임시작 버튼 밑에 배치됨
root.mainloop() #mainloop()를 통해 위젯, 버튼 등이 유지되게끔 한다.



