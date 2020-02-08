# xpath可以解析网页中的内容

# 安装包 lxml 以为网页中的数据
from lxml import etree
if __name__ == '__main__':
    data = '''</script>    <link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/static-common/style/tb.js/dialog_bda1025.css,/tb/static-common/lib/tbui/style/all_f29e774.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/index_4fc89ea.css,/tb/_/search_8bbfc49.css,/tb/_/http_transform_d41d8cd.css,/tb/_/frs-footer/content_footer_e1ac3c2.css,/tb/_/fixed_bar_af8c791.css,/tb/_/fixed_daoliu_c2042f0.css,/tb/_/frs-footer/extension_d41d8cd.css,/tb/_/suggestion_c2d979b.css,/tb/_/page_router_6d81cff.css,/tb/_/login_dialog_32fe58d.css,/tb/_/icons_4bd55ce.css,/tb/_/base_user_data_f665ab7.css,/tb/_/base_dialog_user_bar_69fdf18.css,/tb/_/qianbao_cashier_dialog_179e56e.css,/tb/_/qianbao_purchase_member_f0586a7.css,/tb/_/cashier_dialog_0d74ed0.css,/tb/_/pay_member_d41d8cd.css,/tb/_/new_message_system_bea7f16.css,/tb/_/user_head_35f26e0.css,/tb/_/js_pager_5be1e39.css,/tb/_/wallet_dialog_fce7ffd.css,/tb/_/card_e028cbd.css,/tb/_/userbar_b56525c.css,/tb/_/duoku_servers_dialog_f50364d.css,/tb/_/duoku_servers_list_42e14c2.css,/tb/_/poster/rich_poster_4d57f00.css,/tb/_/footer_fd940ae.css,/tb/_/head_main_6892579.css,/tb/_/full_width_head_ca1a4d5.css,/tb/_/game_head_info_765f80b.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/forum_card_62fcc00.css,/tb/_/qianbao_purchase_tdou_4b31f54.css,/tb/_/payment_dialog_title_5433211.css,/tb/_/tdou_get_1536ffc.css,/tb/_/paykey_safe_payment_8f2a8db.css,/tb/_/captcha_8dce960.css,/tb/_/captcha_safe_payment_d41d8cd.css,/tb/_/mobile_safe_payment_77949bb.css,/tb/_/tbean_safe_3c779a3.css,/tb/_/tbean_safe_ajax_d41d8cd.css,/tb/_/umoney_f12b09a.css,/tb/_/tdou_template_3eae00b.css,/tb/_/umoney_query_d15a716.css,/tb/_/tdou_d41d8cd.css,/tb/_/send_gift_success_24ee666.css,/tb/_/gift_page_ctrl_eac352f.css,/tb/_/gift_loading_css_e2c23e9.css,/tb/_/send_gift_dialog_0b498fd.css,/tb/_/raking_gift_dialog_da61760.css,/tb/_/gift_batou_goin_d46b5b1.css,/tb/_/bubble_tip_8f22754.css,/tb/_/tbshare_share_99dc1ff.css,/tb/_/tbshare_popup_d41d8cd.css,/tb/_/aside_float_bar_e5ad352.css,/tb/_/verify_manager_phone_7d1435e.css,/tb/_/icon_tip_db299f2.css,/tb/_/firework_v2_2e35f90.css,/tb/_/novel_icons_02ab048.css,/tb/_/global_notice_8c177cf.css,/tb/_/umoney_promotion_dialog_d0d023b.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/snowflow_45a89bb.css,/tb/_/dialog_6ed86bb.css,/tb/_/cont_sign_card_73a332e.css,/tb/_/buy_controller_a328148.css,/tb/_/tieba_sign_card_2928c29.css,/tb/_/placeholder_7eb7ce6.css,/tb/_/sms_verify_dialog_cd843b0.css,/tb/_/forbidden_752e552.css,/tb/_/poster/share_thread_cbacfa9.css,/tb/_/like_tip_65eb23b.css,/tb/_/poster/topic_suggestion_c9a8071.css,/tb/_/word_limit_3c5481d.css,/tb/_/complaint_bar_owner_a993083.css,/tb/_/poster/rich_poster_25b39dd.css,/tb/_/ueditor_base_1d8237b.css,/tb/_/ueditor_extend_base_d41d8cd.css,/tb/_/background_c5ba91f.css,/tb/_/tb_gram_d41d8cd.css,/tb/_/slide_select_9a5a934.css,/tb/_/image_flash_editor_8f43e09.css,/tb/_/scroll_panel_eb74727.css,/tb/_/picture_uploader_410491b.css,/tb/_/picture_web_selector_e779653.css,/tb/_/picture_ccc8af7.css,/tb/_/custom_emotion_2d0490a.css,/tb/_/ueditor_emotion_a5eeac8.css,/tb/_/ueditor_video_1453a78.css,/tb/_/sketchpad_fad481d.css,/tb/_/scrawl_5840a35.css,/tb/_/ueditor_topic_bb19767.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/topic_suggestion_3234253.css,/tb/_/fullscreen_a139ec1.css,/tb/_/at_d03b8c9.css,/tb/_/post_setting_46ea748.css,/tb/_/setting_ca19f87.css,/tb/_/medal_5022a4b.css,/tb/_/paypost_agree_dialog_fd57709.css,/tb/_/paypost_editor_6d704da.css,/tb/_/attention_category_game_d2d4220.css,/tb/_/focus_btn_21ad291.css,/tb/_/game_frs_in_head_8026069.css,/tb/_/game_rank_in_head_94ba4ce.css,/tb/_/game_frs_head_218209e.css,/tb/_/tbnav_bright_a02e0ea.css,/tb/_/iframe_head_b5db402.css,/tb/_/activity_btv_2cc5469.css,/tb/_/sign_mod_539e18c.css,/tb/_/sign_tip_98d0754.css,/tb/_/platform_spread_layer_9230140.css,/tb/_/platform_spread_video_846939d.css,/tb/_/top_activity_20d5624.css,/tb/_/popup_zhang_434a867.css,/tb/_/block_user_1e8ac98.css,/tb/_/music_player_526eb38.css,/tb/_/game_code_thread_c9a2228.css,/tb/_/game_thread_d41d8cd.css,/tb/_/single_icons_3112de2.css,/tb/_/post_marry_1ed5b11.css,/tb/_/interaction_d4668aa.css,/tb/_/month_icon_fbf7c06.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/user_visit_card_79e478c.css,/tb/_/util_pop_video_3955ca6.css,/tb/_/voice_fae8e00.css,/tb/_/thread_list_13c3ce3.css,/tb/_/aside_region_6df4cfc.css,/tb/_/frs-aside/app_download_d024b8b.css,/tb/_/lecai_iframe_a48aee4.css,/tb/_/professional_manager_tips_af0267b.css,/tb/_/by_forum_db9c68b.css,/tb/_/thread_item_44be836.css,/tb/_/thread_item_title_a926847.css,/tb/_/frs_user_base_e6ee6b4.css,/tb/_/util_pager_fd327a7.css,/tb/_/thread_list_footer_99af8d2.css,/tb/_/celebrity_widget_974def6.css,/tb/_/celebrity_forum_dialog_b44a28b.css,/tb/_/forum_member_dialog_1d49009.css,/tb/_/exp_package_dialog_5cb5fdb.css,/tb/_/npc_vote_action_5b250b1.css,/tb/_/celebrity_81c8269.css,/tb/_/celebrity_expball_e0bb045.css,/tb/_/frs-aside/forum_info_415639b.css,/tb/_/frs-aside/search_back_2dd1855.css,/tb/_/frs-aside/hottopic_0a620f9.css,/tb/_/mixin_bd9244b.css,/tb/_/bean_d41d8cd.css,/tb/_/guess_3c31a66.css,/tb/_/sidebar_2541a8b.css" />
<link rel="shortcut icon" href="https://gsp0.baidu.com/5aAHeD3nKhI2p27j8IqW0jdnxx1xbK/tb/favicon.ico"/>
'''
    tree = etree.HTML(data)
    # print(tree ,type(tree),etree.tostring(tree).decode('utf-8'),sep = '\n')

    # //查询所有
    # result = tree.xpath('//meta')
    # # print(result)
    # for r in result:
    #     print(etree.tostring(r).decode('utf-8'))

    # /代表查找当前路径
    # result = tree.xpath('/html/head/meta')
    # print('-------',result)
    # for r in result:
    #     print(etree.tostring(r).decode('utf-8'))


    # class 是标签的属性，xpath中使用@表示属性
    # result = tree.xpath('//link[@ral="stylesheet"]')
    # for r in result:
    #     print(etree.tostring(r).decode('utf-8'))
    #

    # 标签
    # result = tree.xpath('//a')
    # for i in result:
    #     print(etree.tostring(r).decode('utf-8'))

    # 获取标签的内容
    # result = tree.xpath('//a/text()')
    # print(result)

    # resylt = tree.xpath('//li[contains(@class,"0")]')
    # for r in result:
    #     print(etree.tostring(r).decode('utf-8'))

    # 获取文件数据
    tree = etree.parse('./data.html')
    # print(etree.tostring(tree,encoding='utf-8').decode('utr-8'))
    # tree.xpath('//li[@id="hehe"]/text()')
    result = tree.xpath('//div[@id="pp"]//li/text()')
    print(result)
    for r in result:
        print(r)
