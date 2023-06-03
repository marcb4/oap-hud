#!/usr/bin/python3
import pygame
import commons.Api_pb2 as oap_api
from commons.Client import Client, ClientEventHandler

description = ""
distance = ""
icon = ""

# OAP API EventHandler
class EventHandler(ClientEventHandler):

    def on_hello_response(self, client, message):
        print(
            "received hello response, result: {}, oap version: {}.{}, api version: {}.{}"
            .format(message.result, message.oap_version.major,
                    message.oap_version.minor, message.api_version.major,
                    message.api_version.minor))

        set_status_subscriptions = oap_api.SetStatusSubscriptions()
        set_status_subscriptions.subscriptions.append(
            oap_api.SetStatusSubscriptions.Subscription.NAVIGATION)
        client.send(oap_api.MESSAGE_SET_STATUS_SUBSCRIPTIONS, 0,
                    set_status_subscriptions.SerializeToString())

    def on_navigation_status(self, client, message):
        print("navigation status: {}, source {}".format(
            message.state, message.source))

    def on_navigation_maneuver_details(self, client, message):
        print("navigation maneuver details, description: {}, icon size: {}".
              format(message.description, len(message.icon)))
        global description
        description = message.description
        global icon
        icon = message.icon

    def on_navigation_maneuver_distance(self, client, message):
        print("navigation maneuver distance, label: {}".format(message.label))
        global distance
        distance = message.label
        


pygame.init()

# Window Size
WIDTH, HEIGHT = 800, 600

# Create window and set to full screen
# window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Navigationssystem")

# Background
bg_color = (0, 0, 0)

# OAP API
client = Client("navigation status example")
event_handler = EventHandler()
client.set_event_handler(event_handler)
client.connect('192.168.4.1', 44405)

# Font
my_font = pygame.font.SysFont('Arial', 60)


running = True
while running:
    try:
        active = client.wait_for_message()
        window.fill(bg_color)

        if len(icon) > 3:
            with open(r'assets/status.png', 'wb') as f:
                f.write(icon)
                print("ICON DISPLAYED")
                image = pygame.image.load('assets/status.png').convert_alpha()
                window.blit(image, (0, 0))  # Pfeil nach links anzeigen
        else:
            print(icon)
            window.blit

        description_surface = my_font.render(description, True, (255, 0, 0))
        window.blit(description_surface, (10,450))

        if distance != "0 m":
            distance_surface = my_font.render(distance, True, (255, 0, 0))
            window.blit(distance_surface, (300,530))

        # Update Display
        pygame.display.flip()

        # Wait for Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    except KeyboardInterrupt:
        break

pygame.quit()
