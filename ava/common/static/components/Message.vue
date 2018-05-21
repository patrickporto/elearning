<template>
    <div>
        <div class="message-group" :class="{ 'me': author.me, 'you': !author.me }" v-if="type == 'chat_message'">
            <img class="author-photo" :src="author.photo" alt="" :title="author.name">
            <div class="messages">
                <div class="message" v-for="(msg, index) in messages" :key="index" @click="like(msg)">
                    <div class="message-inside">
                        <div>
                            {{ msg.content }}
                        </div>
                        <div class="message-reactions" v-if="msg.likes > 0">
                            +{{ msg.likes }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="message-action" v-else>
            <span v-if="type == 'chat_connect'">{{ author.name }} acabou de entrar</span>
            <span v-if="type == 'chat_disconnect'">{{ author.name }} saiu</span>
        </div>
    </div>
</template>

<script>
export default {
    props: ['messages', 'author', 'type', 'sendingDate'],
    methods: {
        like(msg) {
            this.$emit('like', msg.id)
        }
    }
}
</script>

<style lang="sass">
    $action-bg: #A0131C;
    $me-bg: #7A7C7E;
    $you-bg: #800000;

    .message-action {
        display: block;
        color: #A0131C;
        border-radius: 4px;
        padding: 10px;
        position: relative;
        margin: 10px 0;
        text-align: center;
        font-weight: bold;
    }

    .message-reactions {
        background: #f44336;
        border-radius: 4px;
        color: #fff;
        display: inline-block;
        padding: 5px;
        vertical-align: middle;
    }

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
        color: #ffffff;
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
            &-inside {
                background-color: $me-bg;
            }
            &-reactions {
                float: right;
            }
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
                border-left-color: $me-bg;
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
            &-inside {
                background-color: $you-bg;
            }
            &-reactions {
                float: left;
            }
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
                border-right-color: $you-bg;
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
