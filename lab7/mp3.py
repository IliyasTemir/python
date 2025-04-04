import pygame
import os

pygame.init()
pygame.mixer.init()

music_folder = "music"
playlist = [song for song in os.listdir(music_folder) if song.endswith(".mp3")]
playlist.sort()

current_track = 0

def load_and_play(index):
    pygame.mixer.music.load(os.path.join(music_folder, playlist[index]))
    pygame.mixer.music.play()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    load_and_play(current_track)

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    load_and_play(current_track)

def stop():
    pygame.mixer.music.stop()


def play():
    pygame.mixer.music.unpause()


def pause():
    pygame.mixer.music.pause()


load_and_play(current_track)


screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("MP3 Player")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pause()
                else:
                    play()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                prev_track()
            elif event.key == pygame.K_s:
                stop()

    pygame.display.flip()

pygame.quit()
