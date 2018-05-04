<template>
    <div class="message-group" :class="{ 'me': author.me, 'you': !author.me }">
        <img class="author-photo" src="https://placeimg.com/192/192/people" alt="" :title="author.name">
        <div class="messages">
            <div class="message" v-for="(msg, index) in messages" :key="index">
                <div class="message-inside">
                    {{ msg.content }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['messages', 'author'],
}
</script>

<style lang="sass">
    $background-color: #F7F7F7;

    .message-group {
        padding: 20px;
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        align-items: flex-start;
        align-content: center;
    }

    .messages {
        display: inline-block;
        flex: 1;
        margin: 15px;
    }

    .message-inside {
        display: inline-block;
        background: $background-color;
        border-radius: 4px;
        padding: 10px;
        position: relative;
        clear: both;
    }
    .message + .message {
        margin-top: 5px;
    }

    .message-group + .message-group {
        margin-top: 20px;
    }

    .me {
        text-align: right;
        .message {
            order: 0;
            &:first-child .message-inside:after {
                left: 100%;
                top: 50%;
                border: solid transparent;
                content: " ";
                height: 0;
                width: 0;
                position: absolute;
                pointer-events: none;
                border-color: rgba(136, 183, 213, 0);
                border-left-color: $background-color;
                border-width: 10px;
                margin-top: -10px;
            }
        }

        .author-photo {
            order: 1;
        }
    }

    .you {
        text-align: left;
        .message {
            order: 1;
             &:first-child .message-inside:before {
                right: 100%;
                top: 50%;
                border: solid transparent;
                content: " ";
                height: 0;
                width: 0;
                position: absolute;
                pointer-events: none;
                border-color: rgba(136, 183, 213, 0);
                border-right-color: $background-color;
                border-width: 10px;
                margin-top: -10px;
            }
        }
        .author-photo {
            order: 0;
        }
    }

    .author-photo {
        display: inline-block;
        border-radius: 100%;
        max-width: 64px;
    }
</style>
