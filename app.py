from flask import Flask, json, request, jsonify

app = Flask(__name__ )

# img_url = ""
# display_name = ""
# work_time = ""
# phone= ""
# place = ""
# website =""

def create_flex_template(img_url_inp,display_name_inp,work_time_inp,phone_inp,place_inp,website_inp):
    line_template = {
    "type": "bubble",
    "hero": {
        "type": "image",
        "url": img_url_inp,
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": display_name_inp,
            "weight": "bold",
            "size": "xl"
        },
        {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": [
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            },
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            },
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            },
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            },
            {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
            },
            {
                "type": "text",
                "text": "4.0",
                "size": "sm",
                "color": "#999999",
                "margin": "md",
                "flex": 0
            }
            ]
        },
        {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
            {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "Place",
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                },
                {
                    "type": "text",
                    "text": place_inp,
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 5
                }
                ]
            },
            {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "Time",
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                },
                {
                    "type": "text",
                    "text": work_time_inp,
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 5
                }
                ]
            }
            ]
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
                "type": "uri",
                "label": "PHONE",
                "uri": phone_inp
            }
        },
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
                "type": "uri",
                "label": "WEBSITE",
                "uri": website_inp
            }
        },
        {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "margin": "sm"
        }
        ],
        "flex": 0
    }
    }

    return line_template

def createFlex(bubble_json):

    lineres = {
        'type': 'flex',
        'altText': 'This is a Flex message2',
        'contents': {
            "type": "bubble",
            "contents": bubble_json
        }
    }

    payload = {
        "line_payload":[lineres],
        "response_type": "object"
    }
    return payload

@app.route('/')
def index():
    return 'Hello World'

@app.route('/id_card')
def id_card():
    display_name = request.args.get('display_name')
    img_url = request.args.get('img_url')
    place = request.args.get('place')
    work_time = request.args.get('work_time')
    phone = request.args.get('phone')
    website = request.args.get('website')

    flex_message =  create_flex_template(img_url,display_name,work_time,phone,place,website)

    payload = createFlex(flex_message)
    return jsonify(payload)


if __name__ == "__main__":
    app.run(debug=True)
