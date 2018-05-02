<template>
    <div class="message-container" :class="{ 'message--me': author.me }">
        <div class="message-list" :class="{ 'message--me': author.me }">
            <div class="message-content" :class="{ 'message--me': author.me }" v-for="(msg, index) in messages" :key="index"
                :title="contentTitle">
                <div class="message-inside">
                    {{ msg.content }}
                </div>
            </div>
        </div>
        <div class="message-photo" :class="{ 'message--me': author.me }">
            <img :src="author.photo" :title="author.name" />
        </div>
    </div>
</template>

<script>
import moment from 'moment';

moment.locale('pt-BR');

export default {
    props: ['messages', 'author'],
}
</script>

<style lang="sass">
    $background-color: #F7F7F7;

    .message {
        &-inside {
            background: $background-color;
            border-radius: 4px;
            display: inline-block;
            padding: 10px;
        }

        &-content {
            display: block;
            position: relative;

            &.message--me {
                text-align: right;
                &:after {
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
            &:not(.message--me) {
                text-align: left;
                &:after {
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
        }

        &-content + &-content {
            margin-top: 5px;
        }

        &-content + &-content:after,
        &-content + &-content:before {
            content: none;
        }

        &-list {
            display: inline-block;
            position: absolute;
            top: 0;

            &.message--me {
                right: 92px;
            }
            &:not(.message--me) {
                left: 92px;
            }
        }

        &-container {
            position: relative;
        }

        &-container + &-container {
            margin-top: 20px;
        }

        &-photo {
            display: inline-block;
            vertical-align: top;
            position: absolute;
            top: 0;

            &.message--me {
                right: 0;
            }
            &:not(.message--me) {
                left: 0;
            }
            img {
                border-radius: 100%;
                max-width: 64px;
            }
        }
    }
</style>
