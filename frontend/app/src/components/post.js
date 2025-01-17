import { Link } from "react-router-dom";

import { ReactComponent as AvatarImg } from "../images/avatar.svg"
import { ReactComponent as PostImg } from "../images/imagepost.svg"
import { ReactComponent as GlobeImg } from "../images/globe-06.svg"
import { ReactComponent as LikeImg } from "../images/heart.svg"
import { ReactComponent as CommentsImg } from "../images/message-circle-01.svg"
import { ReactComponent as BookmarkImg } from "../images/bookmark.svg"
import { ReactComponent as ReportImg } from "../images/annotation-alert.svg"

const Post = () => {
    return (
        <div class="newsblock">
            <div class="newsblock-header">
                <div class="newsblock-type"><GlobeImg /> Маркетинг</div>
                <div class="newsblock-author"><AvatarImg /> Владимир Желнов</div>
                <div class="newsblock-date">13:34 - Вчера</div>
                <div class="newsblock-subscription">
                    <Link to="#">- Отписаться</Link>
                </div>
            </div>
            <div class="newsblock-content">
                <h2>Пошаговый план создания эффективной рекламной кампании</h2>
                <p>На конец второго квартала группа обслуживала текущие счета более 28,8 млн клиентов, общий остаток средств на них составлял 1,063 трлн рублей. Число клиентов в сфере малого и среднего бизнеса составило 1 млн, на их счетах хранятся 257 млрд рублей.</p>
            </div>
            <div>
                <PostImg />
            </div>
            <div class="newsblock-footer">
                <div class="newsblock-footer__left">
                    <div class="newsblock-footer__cell"><LikeImg /> 1200</div>
                    <div class="newsblock-footer__cell"><CommentsImg /> 65</div>
                </div>
                <div class="newsblock-footer__right">
                    <ReportImg />
                    <BookmarkImg />
                </div>
            </div>
        </div>
    )
}
export default Post;