def berechne_blink_frames(fps, blink_freq, dauer_sek):
    """
    Berechnet Frame-Nummern für ein Blinklicht.
    
    :param fps: Frames pro Sekunde (z.B. 30)
    :param blink_freq: Blinkfrequenz in Hz (z.B. 1 für 1x pro Sekunde)
    :param dauer_sek: Gesamtdauer in Sekunden
    :return: Liste mit Frame-Nummern, bei denen das Licht wechselt
    """
    gesamt_frames = int(fps * dauer_sek)
    blink_interval_frames = int(fps / (blink_freq * 1))  # *2 für Ein/Aus
    
    blink_frames = []
    for frame in range(0, gesamt_frames, blink_interval_frames):
        blink_frames.append(frame)
    
    return blink_frames


# Beispiel-Aufruf
if __name__ == "__main__":
    fps = 12              # Frames pro Sekunde
    blink_freq = 1        # Blinkfrequenz in Hz (2x pro Sekunde)
    dauer_sek = 12        # Dauer in Sekunden

    frames = berechne_blink_frames(fps, blink_freq, dauer_sek)
    
    print(f"Blinkwechsel bei folgenden Frames ({len(frames)} insgesamt):")
    print(frames)