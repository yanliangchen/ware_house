var arrAll =
        [
           {
                name: "请选择国家",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "请选择省",
                        sub: [{name: "地级市、县"}, {name: "请选择市"}],
                        type: 0
                    }], type: 1
            },
            {
                name: "中国",
                sub: [
                    {name: "省份、州", sub: []},
                    {
                        name: "北京",
                        sub: [{name: "地级市、县"},{name: "北京"}],
                        type: 0
                    },
                    {
                        name: "广东",
                        sub: [{name: "地级市、县"},{name: "广州"}, {name: "深圳"}, {name: "珠海"}, {name: "汕头"}, {name: "韶关"}, {name: "佛山"}, {name: "江门"}, {name: "湛江"}, {name: "茂名"}, {name: "肇庆"}, {name: "惠州"}, {name: "梅州"}, {name: "汕尾"}, {name: "河源"},{name:"阳江"},{name:"清远"},{name:"东莞"},{name:"中山"},{name:"潮州"},{name:"揭阳"},{name:"云浮"}],
                        type: 0
                    },
                    {
                        name: "安徽",
                        sub: [{name: "地级市、县"},{name: "安庆"}, {name: "蚌埠"}, {name: "巢湖"}, {name: "池州"}, {name: "滁州"}, {name: "阜阳"}, {name: "合肥"}, {name: "淮北"}, {name: "淮南"}, {name: "黄山"}, {name: "六安"}, {name: "马鞍山"}, {name: "宿州"}, {name: "铜陵"},{name:"芜湖"},{name:"宣城"},{name:"亳州"}],
                        type: 0
                    },
                    {
                        name: "福建",
                        sub: [{name: "地级市、县"},{name: "福州"}, {name: "龙岩"}, {name: "南平"}, {name: "宁德"}, {name: "莆田"}, {name: "泉州"}, {name: "三明"}, {name: "厦门"}, {name: "漳州"}],
                        type: 0
                    },
                    {
                        name: "甘肃",
                        sub: [{name: "地级市、县"},{name: "白银"}, {name: "定西"}, {name: "甘南藏族自治州"}, {name: "嘉峪关"}, {name: "金昌"}, {name: "酒泉"}, {name: "兰州"}, {name: "临夏回族自治州"}, {name: "陇南"}, {name: "平凉"}, {name: "庆阳"}, {name: "天水"}, {name: "武威"}, {name: "张掖"}],
                        type: 0
                    },
                    {
                        name: "广西",
                        sub: [{name: "地级市、县"},{name: "百色"}, {name: "北海"}, {name: "崇左"}, {name: "防城港"}, {name: "桂林"}, {name: "贵港"}, {name: "河池"}, {name: "贺州"}, {name: "来宾"}, {name: "柳州"}, {name: "南宁"}, {name: "钦州"}, {name: "梧州"}, {name: "玉林"}],
                        type: 0
                    },
                    {
                        name: "贵州",
                        sub: [{name: "地级市、县"},{name: "安顺"}, {name: "毕节"}, {name: "贵阳"}, {name: "六盘水"}, {name: "黔东南苗族侗族自治州"}, {name: "黔南布依族苗族自治州"}, {name: "黔西南布依族苗族自治州"}, {name: "铜仁"}, {name: "遵义"}],
                        type: 0
                    },
                    {
                        name: "海南",
                        sub: [{name: "地级市、县"},{name: "白沙黎族自治县"}, {name: "保亭黎族苗族自治县"}, {name: "昌江黎族自治县"}, {name: "澄迈县"}, {name: "定安县"}, {name: "东方"}, {name: "海口"}, {name: "乐东黎族自治县"}, {name: "临高县"}, {name: "陵水黎族自治县"}, {name: "琼海"}, {name: "琼中黎族苗族自治县"}, {name: "三亚"}, {name: "屯昌县"},{name:"万宁"},{name:"文昌"},{name:"五指山"},{name:"儋州"}],
                        type: 0
                    },
                    {
                        name: "河北",
                        sub: [{name: "地级市、县"},{name: "保定"}, {name: "沧州"}, {name: "承德"}, {name: "邯郸"}, {name: "衡水"}, {name: "廊坊"}, {name: "秦皇岛"}, {name: "石家庄"}, {name: "唐山"}, {name: "邢台"}, {name: "张家口"}],
                        type: 0
                    },
                    {
                        name: "河南",
                        sub: [{name: "地级市、县"},{name: "安阳"}, {name: "鹤壁"}, {name: "济源"}, {name: "焦作"}, {name: "开封"}, {name: "洛阳"}, {name: "南阳"}, {name: "平顶山"}, {name: "三门峡"}, {name: "商丘"}, {name: "新乡"}, {name: "信阳"}, {name: "许昌"}, {name: "郑州"},{name:"周口"},{name:"驻马店"},{name:"漯河"},{name:"濮阳"}],
                        type: 0
                    },
                    {
                        name: "黑龙江",
                        sub: [{name: "地级市、县"},{name: "大庆"}, {name: "大兴安岭"}, {name: "哈尔滨"}, {name: "鹤岗"}, {name: "黑河"}, {name: "鸡西"}, {name: "佳木斯"}, {name: "牡丹江"}, {name: "七台河"}, {name: "齐齐哈尔"}, {name: "双鸭山"}, {name: "绥化"}, {name: "伊春"}],
                        type: 0
                    },
                    {
                        name: "湖北",
                        sub: [{name: "地级市、县"},{name: "鄂州"}, {name: "恩施土家族苗族自治州"}, {name: "黄冈"}, {name: "黄石"}, {name: "荆门"}, {name: "荆州"}, {name: "潜江"}, {name: "神农架林区"}, {name: "十堰"}, {name: "随州"}, {name: "天门"}, {name: "武汉"}, {name: "仙桃"}, {name: "咸宁"},{name:"襄樊"},{name:"孝感"},{name:"宜昌"}],
                        type: 0
                    },
                    {
                        name: "湖南",
                        sub: [{name: "地级市、县"},{name: "常德"}, {name: "长沙"}, {name: "郴州"}, {name: "衡阳"}, {name: "怀化"}, {name: "娄底"}, {name: "邵阳"}, {name: "湘潭"}, {name: "湘西土家族苗族自治州"}, {name: "益阳"}, {name: "永州"}, {name: "岳阳"}, {name: "张家界"}, {name: "株洲"}],
                        type: 0
                    },
                    {
                        name: "吉林",
                        sub: [{name: "地级市、县"},{name: "白城"}, {name: "白山"}, {name: "长春"}, {name: "吉林"}, {name: "辽源"}, {name: "四平"}, {name: "松原"}, {name: "通化"}, {name: "延边朝鲜族自治州"}],
                        type: 0
                    },
                    {
                        name: "江苏",
                        sub: [{name: "地级市、县"},{name: "常州"}, {name: "淮安"}, {name: "连云港"}, {name: "南京"}, {name: "南通"}, {name: "苏州"}, {name: "宿迁"}, {name: "泰州"}, {name: "无锡"}, {name: "无锡"}, {name: "盐城"}, {name: "扬州"}, {name: "镇江"}],
                        type: 0
                    },
                    {
                        name: "江西",
                        sub: [{name: "地级市、县"},{name: "抚州"}, {name: "赣州"}, {name: "吉安"}, {name: "景德镇"}, {name: "九江"}, {name: "南昌"}, {name: "萍乡"}, {name: "上饶"}, {name: "新余"}, {name: "宜春"}, {name: "鹰潭"}],
                        type: 0
                    },
                    {
                        name: "辽宁",
                        sub: [{name: "地级市、县"},{name: "鞍山"}, {name: "本溪"}, {name: "朝阳"}, {name: "大连"}, {name: "丹东"}, {name: "抚顺"}, {name: "阜新"}, {name: "葫芦岛"}, {name: "锦州"}, {name: "辽阳"}, {name: "盘锦"}, {name: "沈阳"}, {name: "铁岭"}, {name: "营口"}],
                        type: 0
                    },
                    {
                        name: "内蒙古",
                        sub: [{name: "地级市、县"},{name: "阿拉善盟"}, {name: "巴彦淖尔盟"}, {name: "包头"}, {name: "赤峰"}, {name: "鄂尔多斯"}, {name: "呼和浩特"}, {name: "呼伦贝尔"}, {name: "通辽"}, {name: "乌海"}, {name: "乌兰察布盟"}, {name: "锡林郭勒盟"}, {name: "兴安盟"}],
                        type: 0
                    },
                    {
                        name: "宁夏",
                        sub: [{name: "地级市、县"},{name: "固原"}, {name: "石嘴山"}, {name: "吴忠"}, {name: "银川"}],
                        type: 0
                    },
                    {
                        name: "青海",
                        sub: [{name: "地级市、县"},{name: "果洛藏族自治州"}, {name: "海北藏族自治州"}, {name: "海东"}, {name: "海南藏族自治州"}, {name: "海西蒙古族藏族自治州"}, {name: "黄南藏族自治州"}, {name: "黄南藏族自治州"}, {name: "玉树藏族自治州"}],
                        type: 0
                    },
                    {
                        name: "山东",
                        sub: [{name: "地级市、县"},{name: "滨州"}, {name: "德州"}, {name: "东营"}, {name: "菏泽"}, {name: "菏泽"}, {name: "济宁"}, {name: "莱芜"}, {name: "聊城"}, {name: "临沂"}, {name: "青岛"}, {name: "日照"}, {name: "泰安"}, {name: "威海"}, {name: "潍坊"},{name:"烟台"},{name:"枣庄"},{name:"淄博"}],
                        type: 0
                    },
                    {
                        name: "山西",
                        sub: [{name: "地级市、县"},{name: "长治"}, {name: "大同"}, {name: "晋城"}, {name: "晋中"}, {name: "临汾"}, {name: "吕梁"}, {name: "朔州"}, {name: "太原"}, {name: "忻州"}, {name: "阳泉"}, {name: "运城"}],
                        type: 0
                    },
                    {
                        name: "陕西",
                        sub: [{name: "地级市、县"},{name: "安康"}, {name: "宝鸡"}, {name: "汉中"}, {name: "商洛"}, {name: "铜川"}, {name: "渭南"}, {name: "西安"}, {name: "咸阳"}, {name: "延安"}, {name: "榆林"}],
                        type: 0
                    },
                    {
                        name: "上海",
                        sub: [{name: "地级市、县"},{name: "上海"}],
                        type: 0
                    },
                    {
                        name: "四川",
                        sub: [{name: "地级市、县"},{name: "阿坝藏族羌族自治州"}, {name: "巴中"}, {name: "成都"}, {name: "达州"}, {name: "德阳"}, {name: "甘孜藏族自治州"}, {name: "广安"}, {name: "广元"}, {name: "乐山"}, {name: "凉山彝族自治州"}, {name: "眉山"}, {name: "绵阳"}, {name: "南充"}, {name: "内江"},{name:"攀枝花"},{name:"遂宁"},{name:"雅安"},{name:"宜宾"},{name:"资阳"},{name:"自贡"},{name:"泸州"}],
                        type: 0
                    },
                    {
                        name: "天津",
                        sub: [{name: "地级市、县"},{name: "天津"}],
                        type: 0
                    },
                    {
                        name: "西藏",
                        sub: [{name: "地级市、县"},{name: "阿里"}, {name: "昌都"}, {name: "拉萨"}, {name: "林芝"}, {name: "那曲"}, {name: "日喀则"}, {name: "山南"}],
                        type: 0
                    },
                    {
                        name: "新疆",
                        sub: [{name: "地级市、县"},{name: "阿克苏"}, {name: "阿拉尔"}, {name: "巴音郭楞蒙古自治州"}, {name: "博尔塔拉蒙古自治州"}, {name: "昌吉回族自治州"}, {name: "哈密"}, {name: "和田"}, {name: "喀什"}, {name: "克拉玛依"}, {name: "克孜勒苏柯尔克孜自治州"}, {name: "石河子"}, {name: "图木舒克"}, {name: "吐鲁番"}, {name: "乌鲁木齐"},{name:"五家渠"},{name:"伊犁哈萨克自治州"}],
                        type: 0
                    },
                    {
                        name: "云南",
                        sub: [{name: "地级市、县"},{name: "保山"}, {name: "楚雄彝族自治州"}, {name: "大理白族自治州"}, {name: "德宏傣族景颇族自治州"}, {name: "迪庆藏族自治州"}, {name: "红河哈尼族彝族自治州"}, {name: "昆明"}, {name: "丽江"}, {name: "临沧"}, {name: "怒江傈傈族自治州"}, {name: "曲靖"}, {name: "思茅"}, {name: "文山壮族苗族自治州"}, {name: "西双版纳傣族自治州"},{name:"玉溪"},{name:"昭通"}],
                        type: 0
                    },
                    {
                        name: "浙江",
                        sub: [{name: "地级市、县"},{name: "杭州"}, {name: "湖州"}, {name: "嘉兴"}, {name: "金华"}, {name: "丽水"}, {name: "宁波"}, {name: "绍兴"}, {name: "台州"}, {name: "温州"}, {name: "舟山"}, {name: "衢州"}],
                        type: 0
                    },
                    {
                        name: "重庆",
                        sub: [{name: "地级市、县"},{name: "重庆"}],
                        type: 0
                    }
                    ],
                    type: 1
            },
            {
                name: "韩国",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "汉城特別市",
                        sub: [{name: "地级市、县"},{name: "汉城"}],
                        type: 0
                    },
                    {
                        name: "釜山广域市",
                        sub: [{name: "地级市、县"},{name: "釜山"}, {name: "机张郡"}],
                        type: 0
                    },
                    {
                        name: "大邱广域市",
                        sub: [{name: "地级市、县"},{name: "大邱"}, {name: "达城郡"}],
                        type: 0
                    },
                    {
                        name: "仁川广域市",
                        sub: [{name: "地级市、县"},{name: "仁川"}, {name: "江华郡"}, {name: "瓮津郡"}],
                        type: 0
                    },
                    {
                        name: "光州广域市",
                        sub: [{name: "地级市、县"},{name: "光州"}],
                        type: 0
                    },
                    {
                        name: "大田广域市",
                        sub: [{name: "地级市、县"},{name: "大田"}],
                        type: 0
                    },
                    {
                        name: "蔚山广域市",
                        sub: [{name: "地级市、县"},{name: "蔚山"}, {name: "蔚州郡"}],
                        type: 0
                    },
                    {
                        name: "京畿道",
                        sub: [{name: "地级市、县"},{name: "水原市"}, {name: "城南市"}, {name: "安山市"}, {name: "高阳市"}, {name: "安养市"}, {name: "富川市"}],
                        type: 0
                    },
                    {
                        name: "江原道",
                        sub: [{name: "地级市、县"},{name: "春川市"}, {name: "原州市"}, {name: "江陵市"}],
                        type: 0
                    },
                    {
                        name: "忠清北道",
                        sub: [{name: "地级市、县"},{name: "清州市"}],
                        type: 0
                    },
                    {
                        name: "忠清南道",
                        sub: [{name: "地级市、县"},{name: "天安市"}],
                        type: 0
                    },
                    {
                        name: "全罗北道",
                        sub: [{name: "地级市、县"},{name: "全州市"}, {name: "群山市"}, {name: "益山市"}],
                        type: 0
                    },
                    {
                        name: "全罗南道",
                        sub: [{name: "地级市、县"},{name: "木浦市"}, {name: "丽水市"}, {name: "顺天市"}],
                        type: 0
                    },
                    {
                        name: "庆尚北道",
                        sub: [{name: "地级市、县"},{name: "浦项市"}, {name: "龟尾市"}, {name: "庆州市"}],
                        type: 0
                    },
                    {
                        name: "庆尚南道",
                        sub: [{name: "地级市、县"},{name: "昌原市"}, {name: "马山市"}, {name: "晋州市"}],
                        type: 0
                    },
                    {
                        name: "济州道",
                        sub: [{name: "地级市、县"},{name: "济州市"}, {name: "西归浦市"}, {name: "北济州郡"}, {name: "南济州郡"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "日本",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "东京都",
                        sub: [{name: "地级市、县"}, {name: "东京"}],
                        type: 0
                    },
                    {
                        name: "神奈川县",
                        sub: [{name: "地级市、县"}, {name: "横滨市"}],
                        type: 0
                    },
                    {
                        name: "大阪府",
                        sub: [{name: "地级市、县"}, {name: "大阪市"}],
                        type: 0
                    },
                    {
                        name: "爱知县",
                        sub: [{name: "地级市、县"}, {name: "名古屋市"}],
                        type: 0
                    },
                    {
                        name: "北海道",
                        sub: [{name: "地级市、县"}, {name: "札幌市"}],
                        type: 0
                    },
                    {
                        name: "兵库县",
                        sub: [{name: "地级市、县"}, {name: "神戸市"}],
                        type: 0
                    },
                    {
                        name: "京都府",
                        sub: [{name: "地级市、县"}, {name: "京都市"}],
                        type: 0
                    },
                    {
                        name: "福冈县",
                        sub: [{name: "地级市、县"}, {name: "福冈市"}],
                        type: 0
                    },
                    {
                        name: "神奈川县",
                        sub: [{name: "地级市、县"}, {name: "川崎市"}],
                        type: 0
                    },
                    {
                        name: "埼玉县",
                        sub: [{name: "地级市、县"}, {name: "埼玉市"}],
                        type: 0
                    },
                    {
                        name: "广岛县",
                        sub: [{name: "地级市、县"}, {name: "广岛市"}],
                        type: 0
                    },
                    {
                        name: "宫城县",
                        sub: [{name: "地级市、县"}, {name: "仙台市"}],
                        type: 0
                    },
                    {
                        name: "福冈县",
                        sub: [{name: "地级市、县"}, {name: "北九州市"}],
                        type: 0
                    },
                    {
                        name: "千叶县",
                        sub: [{name: "地级市、县"}, {name: "千叶市"}],
                        type: 0
                    }], type: 1
            },
            {
                name: "新加坡",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "新加坡",
                        sub: [{name: "地级市、县"}, {name: "新加坡"}],
                        type: 0
                    }], type: 1
            },
            {
                name: "马来西亚",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "吉打 Kedah",
                        sub: [{name: "地级市、县"}, {name: "亚罗士打 Alor Setar"}, {name: "浮罗交怡 Langkawi"}, {name: "古邦巴素 Kubang Pasu"}, {name: "巴东得腊 Padang Terap"}, {name: "哥打士打 Kota Setar"}],
                        type: 0
                    },
                    {
                        name: "槟榔屿 Pulau Pinang",
                        sub: [{name: "地级市、县"}, {name: "槟城 George Town"}, {name: "北区（北海） Utara (Butterworth)"}, {name: "中区（大山脚） Tengah (Bkt. Mertajam)"}, {name: "南区（高渊） Selatan (Nibong Tebal)"}, {name: "东北 Timur Laut"}],
                        type: 0
                    },
                    {
                        name: "霹雳 Perak",
                        sub: [{name: "地级市、县"}, {name: "怡保 Ipoh"}, {name: "拉律-马当 Larut & Matang"}, {name: "近打 Kinta"}, {name: "江沙 Kuala Kangsar"}],
                        type: 0
                    },
                    {
                        name: "吉兰丹 Kelantan",
                        sub: [{name: "地级市、县"}, {name: "哥打巴鲁 Kota Baharu"}, {name: "道北 Tumpat"}, {name: "哥登峇鲁 Kota Bharu"}, {name: "巴西马 Pasir Mas"}],
                        type: 0
                    },
                    {
                        name: "丁加奴 Terengganu",
                        sub: [{name: "地级市、县"}, {name: "瓜拉丁加奴 Kuala Terengganu"}, {name: "勿述 Besut"}, {name: "瓜拉丁加奴 Kuala Terengganu"}, {name: "龙运 Dungun"}, {name: "甘马挽 Kemaman"}],
                        type: 0
                    },
                    {
                        name: "彭亨 Pahang",
                        sub: [{name: "地级市、县"}, {name: "关丹 Kuantan"}, {name: "金马仑高原 Cameron Highlands"}, {name: "立卑 Lipis"}, {name: "关丹 Kuantan"}, {name: "而连突 Jerantut"}],
                        type: 0
                    },
                    {
                        name: "雪兰莪 Selangor",
                        sub: [{name: "地级市、县"}, {name: "莎亚南 Shah Alam"}, {name: "沙白安南 Sabak Bernam"}, {name: "乌鲁雪兰莪 Ulu Selangor"}, {name: "瓜拉雪兰莪 Kuala Selangor"}],
                        type: 0
                    },
                    {
                        name: "吉隆坡联邦直辖区 Kuala Lumpur",
                        sub: [{name: "地级市、县"}, {name: "吉隆坡 Kuala Lumpur"}],
                        type: 0
                    },
                    {
                        name: "布特拉再也联邦直辖区 Putrajaya",
                        sub: [{name: "地级市、县"}, {name: "布特拉再也 Putrajaya"}],
                        type: 0
                    },
                    {
                        name: "森美兰 Sembilan",
                        sub: [{name: "地级市、县"}, {name: "芙蓉 Seremban"}, {name: "日叻务 Jelebu"}, {name: "仁保 Jempol"}],
                        type: 0
                    },
                    {
                        name: "马六甲 Melaka",
                        sub: [{name: "地级市、县"}, {name: "马六甲 Melaka"}, {name: "亚罗牙也 Alor Gajah"}],
                        type: 0
                    },
                    {
                        name: "柔佛 Johor",
                        sub: [{name: "地级市、县"}, {name: "新山 Johor Baharu"}, {name: "昔加末 Segamat"}, {name: "丰盛港 Mersing"}, {name: "居銮 Keluang"}],
                        type: 0
                    },
                    {
                        name: "斗湖省 Tawau",
                        sub: [{name: "地级市、县"}, {name: "斗湖 Tawau"}, {name: "拿笃 Lahad Datu"}],
                        type: 0
                    },
                    {
                        name: "山打根省 Sandakan",
                        sub: [{name: "地级市、县"}, {name: "山打根 Sandakan"}, {name: "京那巴登岸 Kinabatangan"}],
                        type: 0
                    },
                    {
                        name: "西海岸省 Pantai Barat",
                        sub: [{name: "地级市、县"}, {name: "哥打京那峇鲁（亚庇） Kota Kinabalu"}, {name: "兰脑 Ranau"}, {name: "古打毛律 Kota Belud"}, {name: "斗亚兰 Tuaran"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "菲律宾",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "伊罗戈斯 Ilocos",
                        sub: [{name: "地级市、县"}, {name: "圣费尔南多* San Fernando"}],
                        type: 0
                    },
                    {
                        name: "卡加延河谷 Cagayan",
                        sub: [{name: "地级市、县"}, {name: "土格加劳 Tuguegarao"}],
                        type: 0
                    },
                    {
                        name: "中央吕宋 Central Luzon",
                        sub: [{name: "地级市、县"}, {name: "圣费尔南多* San Fernando"}],
                        type: 0
                    },
                    {
                        name: "甲拉巴松 Calabarzon",
                        sub: [{name: "地级市、县"}, {name: "奎松城 Quezon"}],
                        type: 0
                    },
                    {
                        name: "比科尔 Bicol",
                        sub: [{name: "地级市、县"}, {name: "黎牙实比 Legaspi"}],
                        type: 0
                    },
                    {
                        name: "西米沙鄢 Western Visayas",
                        sub: [{name: "地级市、县"}, {name: "伊洛伊洛 Legaspi"}],
                        type: 0
                    },
                    {
                        name: "中米沙鄢 Central Visayas",
                        sub: [{name: "地级市、县"}, {name: "宿务 Cebu"}],
                        type: 0
                    },
                    {
                        name: "东米沙鄢 Eastern Visayas",
                        sub: [{name: "地级市、县"}, {name: "塔克洛班 Tacloban"}],
                        type: 0
                    },
                    {
                        name: "国家首都区 National Capital Region",
                        sub: [{name: "地级市、县"}, {name: "马尼拉 Manila"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "沙特阿拉伯",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "利雅得 Ar Riyad",
                        sub: [{name: "地级市、县"}, {name: "利雅得 Riyad"},{name: "海耶 Al-Kharj"}],
                        type: 0
                    },
                    {
                        name: "麦加 Makkah",
                        sub: [{name: "地级市、县"}, {name: "麦加 Makkah"},{name: "吉达 Jiddah"},{name: "塔伊夫 At-Ta'if"}],
                        type: 0
                    },
                    {
                        name: "麦地那 Al Madinah",
                        sub: [{name: "地级市、县"}, {name: "麦地那 Madinah"},{name: "延布 Yanbu' al-Bahr"}],
                        type: 0
                    },
                    {
                        name: "东部 Ash Sharqiyah",
                        sub: [{name: "地级市、县"}, {name: "达曼 Dammam"}, {name: "胡富夫 Al-Hufūf"}, {name: "姆巴拉兹 Al-Mubarraz"}, {name: "朱拜勒 Al-Jubayl"}, {name: "哈费尔巴廷 Hafar al-Bātin"}],
                        type: 0
                    },
                    {
                        name: "卡西姆 Al Qasim",
                        sub: [{name: "地级市、县"}, {name: "布赖代 Buraydah"}],
                        type: 0
                    },
                    {
                        name: "哈伊勒 Ha'il",
                        sub: [{name: "地级市、县"}, {name: "哈伊勒 Ha'il"}],
                        type: 0
                    },
                    {
                        name: "塔布克 Tabuk",
                        sub: [{name: "地级市、县"}, {name: "塔布克 Tabuk"}],
                        type: 0
                    },
                    {
                        name: "北部边疆 Al Hudud ash Shamaliyah",
                        sub: [{name: "地级市、县"}, {name: "阿尔阿尔 Ar'ar"}],
                        type: 0
                    },
                    {
                        name: "吉赞 Jizan",
                        sub: [{name: "地级市、县"}, {name: "吉赞 Jizan"}],
                        type: 0
                    },
                    {
                        name: "纳季兰 Najran",
                        sub: [{name: "地级市、县"}, {name: "纳季兰 Najran"}],
                        type: 0
                    },
                    {
                        name: "巴哈 Al Bahah",
                        sub: [{name: "地级市、县"}, {name: "巴哈 Al Bahah"}],
                        type: 0
                    },
                    {
                        name: "朱夫 Al Jawf",
                        sub: [{name: "地级市、县"}, {name: "塞卡卡 Sakaka"}],
                        type: 0
                    },
                    {
                         name: "阿西尔 ‘Asir",
                        sub: [{name: "地级市、县"}, {name: "艾卜哈 Abhā"}, {name: "海米斯穆谢特 Khamīs Mushayt"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "朝鲜",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "平壤直辖市",
                        sub: [{name: "地级市、县"}, {name: "平壤"}],
                        type: 0
                    },
                    {
                        name: "罗先直辖市",
                        sub: [{name: "地级市、县"}, {name: "罗津"}],
                        type: 0
                    },
                    {
                        name: "平安南道",
                        sub: [{name: "地级市、县"}, {name: "南浦特级市"}, {name: "平城市"}, {name: "顺川市"}, {name: "德川市"}, {name: "安州市"}, {name: "价川市"}],
                        type: 0
                    },
                    {
                        name: "平安北道",
                        sub: [{name: "地级市、县"}, {name: "新义州市"}, {name: "龟城市"}, {name: "定州市"}],
                        type: 0
                    },
                    {
                        name: "慈江道",
                        sub: [{name: "地级市、县"}, {name: "江界市"}, {name: "满浦市"}, {name: "煕川市"}],
                        type: 0
                    },
                    {
                        name: "两江道",
                        sub: [{name: "地级市、县"}, {name: "恵山市"}],
                        type: 0
                    },
                    {
                        name: "咸镜北道",
                        sub: [{name: "地级市、县"}, {name: "清津市"}, {name: "金策市"}, {name: "会宁市"}],
                        type: 0
                    },
                    {
                        name: "咸镜南道",
                        sub: [{name: "地级市、县"}, {name: "咸兴市"}, {name: "兴南市"}, {name: "新浦市"}, {name: "端川市"}],
                        type: 0
                    },
                    {
                        name: "黄海北道",
                        sub: [{name: "地级市、县"}, {name: "沙里院市"}, {name: "松林市"}, {name: "开城市"}],
                        type: 0
                    },
                    {
                        name: "黄海南道",
                        sub: [{name: "地级市、县"}, {name: "海州市"}],
                        type: 0
                    },
                    {
                        name: "江原道",
                        sub: [{name: "地级市、县"}, {name: "元山市"}, {name: "文川市"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "越南",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "河内市",
                        sub: [{name: "地级市、县"}, {name: "河内市"}],
                        type: 0
                    },
                    {
                        name: "山罗",
                        sub: [{name: "地级市、县"}, {name: "山罗"}],
                        type: 0
                    },
                    {
                        name: "奠边",
                        sub: [{name: "地级市、县"}, {name: "奠边府市"}, {name: "孟雷"}],
                        type: 0
                    },
                    {
                        name: "谅山",
                        sub: [{name: "地级市、县"}, {name: "谅山市"}],
                        type: 0
                    },
                    {
                        name: "河西",
                        sub: [{name: "地级市、县"}, {name: "河东"}, {name: "山西"}],
                        type: 0
                    },
                    {
                        name: "清化",
                        sub: [{name: "地级市、县"}, {name: "清化市"}, {name: "岑山"}, {name: "拜尚"}],
                        type: 0
                    },
                    {
                        name: "义安",
                        sub: [{name: "地级市、县"}, {name: "荣市"}, {name: "扩路"}],
                        type: 0
                    },
                    {
                        name: "广南",
                        sub: [{name: "地级市、县"}, {name: "三歧"}, {name: "会安"}],
                        type: 0
                    },
                    {
                        name: "嘉莱",
                        sub: [{name: "地级市、县"}, {name: "波来古市"}, {name: "安溪"}],
                        type: 0
                    },
                    {
                        name: "多乐",
                        sub: [{name: "地级市、县"}, {name: "邦美蜀市"}],
                        type: 0
                    },
                    {
                        name: "平福",
                        sub: [{name: "地级市、县"}, {name: "东帅"}],
                        type: 0
                    },
                    {
                        name: "金瓯",
                        sub: [{name: "地级市、县"}, {name: "金瓯市"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "缅甸",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "实皆省 Sagaing",
                        sub: [{name: "地级市、县"}, {name: "实皆 Sagaing"}],
                        type: 0
                    },
                    {
                        name: "望濑县 Monywa",
                        sub: [{name: "地级市、县"}, {name: "望濑 Monywa"}],
                        type: 0
                    },
                    {
                        name: "勃固省 Bago",
                        sub: [{name: "地级市、县"}, {name: "勃固 Bago"}],
                        type: 0
                    },
                    {
                        name: "马圭省 Magway",
                        sub: [{name: "地级市、县"}, {name: "马圭 Magway"}],
                        type: 0
                    },
                    {
                        name: "曼德勒省 Mandalay",
                        sub: [{name: "地级市、县"}, {name: "曼德勒 Mandalay"}],
                        type: 0
                    },
                    {
                        name: "德林达依省 Tanintharyi",
                        sub: [{name: "地级市、县"}, {name: "土瓦 Dawei"}],
                        type: 0
                    },
                    {
                        name: "伊洛瓦底省 Ayeyarwady",
                        sub: [{name: "地级市、县"}, {name: "勃生 Pathein"}],
                        type: 0
                    },
                    {
                        name: "仰光省 Yangon",
                        sub: [{name: "地级市、县"}, {name: "仰光 Yangan "}],
                        type: 0
                    },
                    {
                        name: "克钦邦 Kachin",
                        sub: [{name: "地级市、县"}, {name: "密支那 Myitkyina"}],
                        type: 0
                    },
                    {
                        name: "克耶邦 Kayah",
                        sub: [{name: "地级市、县"}, {name: "垒固 Loi-kaw"}],
                        type: 0
                    },
                    {
                        name: "克伦邦 Kayin",
                        sub: [{name: "地级市、县"}, {name: "巴安 Pa-an"}],
                        type: 0
                    },
                    {
                        name: "钦邦 Chin",
                        sub: [{name: "地级市、县"}, {name: "哈卡 Haka"}],
                        type: 0
                    },
                    {
                        name: "孟邦 Mon",
                        sub: [{name: "地级市、县"}, {name: "毛淡棉 Mawlamyine"}],
                        type: 0
                    },
                    {
                        name: "若开邦 Rakhine",
                        sub: [{name: "地级市、县"}, {name: "实兑 Akyab"}],
                        type: 0
                    },
                    {
                        name: "掸邦 Shan",
                        sub: [{name: "地级市、县"}, {name: "东枝 Taunggyi"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "德国",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "巴登-符腾堡 Baden-Württemberg",
                        sub: [{name: "地级市、县"}, {name: "斯图加特  Stuttgart"}, {name: "卡尔斯鲁厄 Karlsruhe"}, {name: "弗赖堡 Freiburg"}, {name: "图宾根 Tübingen"}],
                        type: 0
                    },
                    {
                        name: "拜恩（巴伐利亚）  Bayern",
                        sub: [{name: "地级市、县"}, {name: "慕尼黑 München "}, {name: "下拜恩 Niederbayern"}, {name: "上普法尔茨 Oberpfalz"}, {name: "上弗兰肯 Oberfranken"}, {name: "中弗兰肯 Mittelfranken"}, {name: "外弗兰肯 Unterfranken"}, {name: "施瓦本 Schwaben"}],
                        type: 0
                    },
                    {
                        name: "柏 林 Berlin",
                        sub: [{name: "地级市、县"}, {name: "柏林 Berlin"}],
                        type: 0
                    },
                    {
                        name: "勃兰登堡 Brandenburg",
                        sub: [{name: "地级市、县"}, {name: "波茨坦 Potsdam"}],
                        type: 0
                    },
                    {
                        name: "不来梅 Bremen",
                        sub: [{name: "地级市、县"}, {name: "不来梅 Bremen"}],
                        type: 0
                    },
                    {
                        name: "汉 堡 Hamburg",
                        sub: [{name: "地级市、县"}, {name: "汉堡 Hamburg"}],
                        type: 0
                    },
                    {
                        name: "黑 森 Hessen",
                        sub: [{name: "地级市、县"}, {name: "达姆施塔特 Darmstadt"}, {name: "吉森 Gieben"}, {name: "卡塞尔 Kassel"}],
                        type: 0
                    },
                    {
                        name: "梅克伦堡-前波莫瑞 Mecklenburg-Vorpommern",
                        sub: [{name: "地级市、县"}, {name: "什未林 Schwerin"}],
                        type: 0
                    },
                    {
                        name: "下萨克森  Niedersachsen",
                        sub: [{name: "地级市、县"}, {name: "不伦瑞克 Braunschweig"}, {name: "汉诺威  Hannover"}],
                        type: 0
                    },
                    {
                        name: "北莱茵-威斯特法伦 Nordrhein-Westfalen",
                        sub: [{name: "地级市、县"}, {name: "杜塞尔多夫 Düsseldorf"}, {name: "科隆 Koln"}, {name: "明斯特 Münster"}, {name: "代特莫尔特 Detmold"}],
                        type: 0
                    },
                    {
                        name: "莱茵兰-普法尔茨 Rheinland-Pfalz",
                        sub: [{name: "地级市、县"}, {name: "科布伦次 Koblenz "}, {name: "特里尔 Trier"}, {name: "莱茵黑森-普法尔茨"}],
                        type: 0
                    },
                    {
                        name: "萨 尔 Saarland",
                        sub: [{name: "地级市、县"}, {name: "萨尔布吕肯 Saarbrücken"}],
                        type: 0
                    },
                    {
                        name: "萨克森 Sachsen",
                        sub: [{name: "地级市、县"}, {name: "开姆尼斯 Chemnitz"}, {name: "德累斯顿 Dresden"}, {name: "莱比锡 Leipzig"}],
                        type: 0
                    },
                    {
                        name: "萨克森-安哈特 Sachsen-Anhalt",
                        sub: [{name: "地级市、县"}, {name: "德绍 Dessau"}, {name: "哈雷 Halle"}, {name: "马格德堡 Magdeburg"}],
                        type: 0
                    },
                    {
                        name: "石勒苏益格-荷尔斯泰因 Schleswig-Holstein",
                        sub: [{name: "地级市、县"}, {name: "基尔 Kiel"}],
                        type: 0
                    },
                    {
                        name: "图林根 Thüringen",
                        sub: [{name: "地级市、县"}, {name: "埃尔富特 Erfurt"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "英国",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "英格兰 England",
                        sub: [{name: "地级市、县"}, {name: "坎布里亚 Cumbria"}, {name: "兰开夏 Lancashire"}, {name: "布莱克本 Blackburn with Darwen"}, {name: "大曼彻斯特 Greater Manchester"}, {name: "柴郡 Cheshire "}, {name: "诺森伯兰 Northumberland"}, {name: "达勒姆 Durham"}, {name: "北约克郡 North Yorkshire"}, {name: "约克郡东区 East Riding of Yorkshire"}, {name: "西约克郡 West Yorkshire"}, {name: "南约克郡 South Yorkshire"}, {name: "林肯郡 Lincolnshire"}, {name: "诺丁汉郡 Nottinghamshire"}, {name: "南约克郡 South Yorkshire"}, {name: "斯塔福德郡 Staffordshire"}, {name: "诺福克 Norfolk"}, {name: "伦敦 London"}, {name: "白金汉郡 Buckinghamshire"}, {name: "牛津郡 Oxfordshire"}, {name: "格洛斯特郡 Gloucestershire"}],
                        type: 0
                    },
                    {
                        name: "威尔士 Wales",
                        sub: [{name: "地级市、县"}, {name: "康威 Conwy *"}, {name: "圭内斯 Gwynedd"}, {name: "锡尔迪金 Ceredigion"}, {name: "波伊斯 Powys"}, {name: "彭布罗克郡 Pembrokeshire"}, {name: "卡马森郡 Carmarthenshire"}],
                        type: 0
                    },
                    {
                        name: "苏格兰 Scotland",
                        sub: [{name: "地级市、县"}, {name: "苏格兰高地 Highland"}, {name: "马里 Moray"}, {name: "阿伯丁郡 Aberdeenshire"}, {name: "安格斯 Angus"}, {name: "珀斯-金罗斯 Perth and Kinross"}, {name: "法夫 Fife"}, {name: "斯特灵 Stirling"}, {name: "阿盖尔-比特 Argyll and Bute"}, {name: "苏格兰边界 Scottish Borders"}, {name: "邓弗里斯-加洛韦 Dumfries and Galloway"}],
                        type: 0
                    },
                    {
                        name: "北爱尔兰 Northern Ireland",
                        sub: [{name: "地级市、县"}, {name: "阿兹 Ards"}, {name: "卡斯尔雷 Castlereagh"}, {name: "唐 Down"}, {name: "贝尔法斯特 Belfast, City of"}, {name: "利斯本 Lisburn"}, {name: "巴利米纳 Ballymena"}, {name: "莫伊尔 Moyle"}, {name: "阿马 Armagh"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "法国",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "法兰西岛 Ile-de-France",
                        sub: [{name: "地级市、县"}, {name: "巴黎 Paris"}],
                        type: 0
                    },
                    {
                        name: "香槟-阿登 Champagne-Ardenn",
                        sub: [{name: "地级市、县"}, {name: "兰斯 Reims"}],
                        type: 0
                    },
                    {
                        name: "皮卡第 Picardie",
                        sub: [{name: "地级市、县"}, {name: "亚眠 Ameiens"}],
                        type: 0
                    },
                    {
                        name: "上诺曼底 Haute-Normandie",
                        sub: [{name: "地级市、县"}, {name: "鲁昂 Rouen"}],
                        type: 0
                    },
                    {
                        name: "中央 Centre",
                        sub: [{name: "地级市、县"}, {name: "奥尔良 Orléans"}],
                        type: 0
                    },
                    {
                        name: "下诺曼底 Basse-Normandie",
                        sub: [{name: "地级市、县"}, {name: "卡昂 Caen"}],
                        type: 0
                    },
                    {
                        name: "勃艮第 Bourgogne",
                        sub: [{name: "地级市、县"}, {name: "第戎 Dijon"}],
                        type: 0
                    },
                    {
                        name: "北部-加莱海峡 Nord-pas-de-Calais",
                        sub: [{name: "地级市、县"}, {name: "里尔 Lille"}],
                        type: 0
                    },
                    {
                        name: "洛林 Lorraine",
                        sub: [{name: "地级市、县"}, {name: "南锡 Nancy"}],
                        type: 0
                    },
                    {
                        name: "阿尔萨斯 Alsace",
                        sub: [{name: "地级市、县"}, {name: "斯特拉斯堡 Strasbourg"}],
                        type: 0
                    },
                    {
                        name: "弗朗什孔泰 Franche-Comté",
                        sub: [{name: "地级市、县"}, {name: "贝桑松 Besancon"}],
                        type: 0
                    },
                    {
                        name: "卢瓦尔河地区 Pays de la Loire",
                        sub: [{name: "地级市、县"}, {name: "南特 Nantes"}],
                        type: 0
                    },
                    {
                        name: "布列塔尼 Bretagne",
                        sub: [{name: "地级市、县"}, {name: "雷恩 Rennes"}],
                        type: 0
                    },
                    {
                        name: "普瓦图-夏朗德 Poitou-Charentes",
                        sub: [{name: "地级市、县"}, {name: "普瓦捷 Poitiers"}],
                        type: 0
                    },
                    {
                        name: "阿基坦 Aquitaine",
                        sub: [{name: "地级市、县"}, {name: "波尔多 Bordeaux"}],
                        type: 0
                    },
                    {
                        name: "南部-比利牛斯 Midi-Pyrénées",
                        sub: [{name: "地级市、县"}, {name: "图卢兹 Toulouse"}],
                        type: 0
                    },
                    {
                        name: "利穆赞 Limousin",
                        sub: [{name: "地级市、县"}, {name: "利摩日 Limoges"}],
                        type: 0
                    },
                    {
                        name: "罗讷-阿尔卑斯 Rhone-Alpes",
                        sub: [{name: "地级市、县"}, {name: "里昂 Lyon"}],
                        type: 0
                    },
                    {
                        name: "奥弗涅 Auvergne",
                        sub: [{name: "地级市、县"}, {name: "克莱蒙费朗 Clerment-Ferrand"}],
                        type: 0
                    },
                    {
                        name: "朗格多克-鲁西永 Languedoc-Roussillon",
                        sub: [{name: "地级市、县"}, {name: "蒙彼里埃 Montpellier"}],
                        type: 0
                    },
                    {
                        name: "普罗旺斯-阿尔卑斯-蓝色海岸 Provence-Alpes-Cote d'Azur",
                        sub: [{name: "地级市、县"}, {name: "马赛 Marseille"}],
                        type: 0
                    },
                    {
                        name: "科西嘉 Corse",
                        sub: [{name: "地级市、县"}, {name: "阿雅克肖 Ajaccio"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "爱尔兰",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "穆斯特省 Munster",
                        sub: [{name: "地级市、县"}, {name: "科克 Cork"}, {name: "沃特福德 Waterford"}, {name: "利默里克 Limerick"}, {name: "凯里 Kerry"}, {name: "蒂珀雷里 Tipperary"}, {name: "克莱尔 Clare"}],
                        type: 0
                    },
                    {
                        name: "康诺特省 Connacht",
                        sub: [{name: "地级市、县"}, {name: "戈尔韦 Galway"}, {name: "梅奥 Mayo"}, {name: "罗斯康芒  Roscommon"}, {name: "利特里姆  Leitrim"}, {name: "斯莱戈 Sligo"}],
                        type: 0
                    },
                    {
                        name: "伦斯特省 Leinster",
                        sub: [{name: "地级市、县"}, {name: "都柏林 Dublin"}, {name: "基尔代尔 Kildare"}, {name: "米斯 Meath"}, {name: "威克洛 Wicklow"}, {name: "西米斯 Westmeath"}, {name: "卡范 Cavan"}, {name: "朗福德 Longford"}, {name: "奥法利  Offaly"}, {name: "崂斯  Laoighis"}, {name: "卡洛 Carlow"}, {name: "基尔肯尼 Kilkenny"}, {name: "韦克斯福德 Wexford"}],
                        type: 0
                    },
                    {
                        name: "阿尔斯特省 Ulster",
                        sub: [{name: "地级市、县"}, {name: "劳斯 Louth"}, {name: "多内加尔 Donegal"}, {name: "莫内根 Monaghan"}, {name: "阿马 Armagh"}, {name: "安特里姆 Antrim"}, {name: "德里 Derry"}, {name: "唐 Down"}, {name: "泰隆 Tyrone"}, {name: "弗马纳 Fermanagh"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "波兰",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "下西里西亚 Dolnoslaskie",
                        sub: [{name: "地级市、县"}, {name: "弗罗茨瓦夫"}, {name: "耶莱尼亚古拉"}, {name: "瓦乌布日赫"}, {name: "莱格尼察"}],
                        type: 0
                    },
                    {
                        name: "库亚瓦滨海 Kujawsko-Pomorskie",
                        sub: [{name: "地级市、县"}, {name: "比得哥什"}, {name: "托伦"}, {name: "格鲁琼兹"}, {name: "弗沃茨瓦韦克"}],
                        type: 0
                    },
                    {
                        name: "罗兹 Lódzkie",
                        sub: [{name: "地级市、县"}, {name: "罗兹"}, {name: "彼得库夫"}, {name: "斯凯尔涅维采"}, {name: "谢拉兹"}],
                        type: 0
                    },
                    {
                        name: "卢布林 Lubelskie",
                        sub: [{name: "地级市、县"}, {name: "卢布林"}, {name: "海乌姆"}, {name: "扎莫希奇"}, {name: "比亚瓦波德拉斯卡"}],
                        type: 0
                    },
                    {
                        name: "鲁布斯卡 Lubuskie",
                        sub: [{name: "地级市、县"}, {name: "绿山城"}, {name: "大波兰地区戈茹夫"}],
                        type: 0
                    },
                    {
                        name: "小波兰 Malopolskie",
                        sub: [{name: "地级市、县"}, {name: "克拉科夫"}, {name: "塔尔努夫"}, {name: "新松奇"}],
                        type: 0
                    },
                    {
                        name: "马佐夫舍 Mazowieckie",
                        sub: [{name: "地级市、县"}, {name: "华沙"}, {name: "切哈努夫"}, {name: "普沃茨克"}, {name: "奥斯特罗文卡"}, {name: "谢德尔采"}, {name: "拉多姆"}],
                        type: 0
                    },
                    {
                        name: "奥波莱 Opolskie",
                        sub: [{name: "地级市、县"}, {name: "奥波莱"}],
                        type: 0
                    },
                    {
                        name: "喀尔巴阡山 Podkarpackie",
                        sub: [{name: "地级市、县"}, {name: "热舒夫"}, {name: "塔尔诺布热格"}, {name: "克罗斯诺"}, {name: "普热梅希尔"}],
                        type: 0
                    },
                    {
                        name: "波德拉斯 Podlaskie",
                        sub: [{name: "地级市、县"}, {name: "比亚维斯托克"}, {name: "苏瓦乌基"}, {name: "沃姆扎"}],
                        type: 0
                    },
                    {
                        name: "滨海 Pomorskie",
                        sub: [{name: "地级市、县"}, {name: "格但斯克"}, {name: "格丁尼亚"}, {name: "索波特"}, {name: "斯武普斯克"}],
                        type: 0
                    },
                    {
                        name: "西里西亚 Slaskie",
                        sub: [{name: "地级市、县"}, {name: "卡托维兹"}, {name: "琴斯托霍瓦"}, {name: "别尔斯科-比亚瓦"}, {name: "雷布尼克"}, {name: "索斯诺维茨"}, {name: "格利维采"}, {name: "比托姆"}],
                        type: 0
                    },
                    {
                        name: "圣十字 Swietokrzyskie",
                        sub: [{name: "地级市、县"}, {name: "凯尔采"}],
                        type: 0
                    },
                    {
                        name: "瓦尔米亚马祖尔 Warmińsko-Mazurskie",
                        sub: [{name: "地级市、县"}, {name: "奥尔什丁"}, {name: "埃尔布隆格"}],
                        type: 0
                    },
                    {
                        name: "大波兰 Wielkopolskie",
                        sub: [{name: "地级市、县"}, {name: "波兹南"}, {name: "皮瓦"}, {name: "卡利什"}, {name: "莱什诺"}, {name: "科宁"}],
                        type: 0
                    },
                    {
                        name: "西滨海 Zachodniopomorskie",
                        sub: [{name: "地级市、县"}, {name: "什切青"}, {name: "科沙林"}, {name: "希维诺乌伊希切"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "西班牙",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "安达卢西亚 Andalucía",
                        sub: [{name: "地级市、县"}, {name: "阿尔梅里亚 Almería"}, {name: "加的斯 Cádiz"}, {name: "科尔多瓦 Córdoba"}, {name: "格拉纳达 Granada"}, {name: "韦尔瓦 Huelva"}, {name: "哈恩 Jáen"}, {name: "马拉加 Málaga"}, {name: "塞维利亚 Sevilla"}],
                        type: 0
                    },
                    {
                        name: "阿拉贡 Aragón",
                        sub: [{name: "地级市、县"}, {name: "韦斯卡 Huesca"}, {name: "特鲁埃尔 Teruel"}, {name: "萨拉戈萨 Zaragoza"}],
                        type: 0
                    },
                    {
                        name: "阿斯图利亚斯 Asturias",
                        sub: [{name: "地级市、县"}, {name: "奥维耶多 Oviedo"}],
                        type: 0
                    },
                    {
                        name: "巴利阿里群岛 Baleares",
                        sub: [{name: "地级市、县"}, {name: "巴利阿里 Baleares"}],
                        type: 0
                    },
                    {
                        name: "加那利 Canarias",
                        sub: [{name: "地级市、县"}, {name: "拉斯帕尔马斯 Las Palmas"}, {name: "圣克鲁斯-德特内里费 Santa Cruz de Tenerife"}],
                        type: 0
                    },
                    {
                        name: "坎塔布利亚 Cantábria",
                        sub: [{name: "地级市、县"}, {name: "桑坦德 Santander"}],
                        type: 0
                    },
                    {
                        name: "卡斯蒂利亚－拉曼恰 Castilla-La Mancha",
                        sub: [{name: "地级市、县"}, {name: "阿尔瓦塞特 Albacete"}, {name: "雷阿尔城 Ciudad Real"}, {name: "昆卡 Cuenca"}, {name: "瓜达拉哈拉 Guadalajara"}, {name: "托莱多 Toledo"}],
                        type: 0
                    },
                    {
                        name: "卡斯蒂利亚－莱昂 Castilla y Léon",
                        sub: [{name: "地级市、县"}, {name: "阿维拉 ávila"}, {name: "布尔戈斯 Burgos"}, {name: "莱昂 León"}, {name: "帕伦西亚 Palencia"}, {name: "萨拉曼卡 Salamanca"}, {name: "塞哥维亚 Segovia"}, {name: "索里亚 Soria"}, {name: "巴利亚多利德 Valladolid"}, {name: "萨莫拉 Zamora"}],
                        type: 0
                    },
                    {
                        name: "加泰罗尼亚* Cataluna",
                        sub: [{name: "地级市、县"}, {name: "巴塞罗那 Barcelona"}, {name: "赫罗纳 Gerona"}, {name: "莱里达 Lérida"}, {name: "塔拉戈纳 Tarragona"}],
                        type: 0
                    },
                    {
                        name: "加利西亚* Galicia",
                        sub: [{name: "地级市、县"}, {name: "拉科鲁尼亚 A Coruna"}, {name: "卢戈 Lugo"}, {name: "奥伦塞 Ourense"}, {name: "蓬特韦德拉 Pontevedra"}],
                        type: 0
                    },
                    {
                        name: "马德里 Madrid",
                        sub: [{name: "地级市、县"}, {name: "马德里 Madrid"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "意大利",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "阿布鲁佐 Abruzzi",
                        sub: [{name: "地级市、县"}, {name: "拉奎拉 L'Aquila"}],
                        type: 0
                    },
                    {
                        name: "巴西利卡塔 Basilicata",
                        sub: [{name: "地级市、县"}, {name: "波坦察 Potenza"}],
                        type: 0
                    },
                    {
                        name: "卡拉布里亚 Calabria",
                        sub: [{name: "地级市、县"}, {name: "卡坦扎罗 Catanzaro"}],
                        type: 0
                    },
                    {
                        name: "坎帕尼亚 Campania",
                        sub: [{name: "地级市、县"}, {name: "那波利 Napoli"}],
                        type: 0
                    },
                    {
                        name: "艾米利亚－罗马涅 Emilia-Romagna",
                        sub: [{name: "地级市、县"}, {name: "博洛尼亚 Bologna"}],
                        type: 0
                    },
                    {
                        name: "弗留利－威尼斯·朱利亚* Friuli-Venezia Giulia",
                        sub: [{name: "地级市、县"}, {name: "的里雅斯特 Trieste"}],
                        type: 0
                    },
                    {
                        name: "拉齐奥 Lazio",
                        sub: [{name: "地级市、县"}, {name: "罗马 Roma"}],
                        type: 0
                    },
                    {
                        name: "利古里亚 Liguria",
                        sub: [{name: "地级市、县"}, {name: "热那亚 Genova"}],
                        type: 0
                    },
                    {
                        name: "伦巴第 Lombardia",
                        sub: [{name: "地级市、县"}, {name: "米兰 Milano"}],
                        type: 0
                    },
                    {
                        name: "马尔凯 Marche",
                        sub: [{name: "地级市、县"}, {name: "安科纳 Ancona"}],
                        type: 0
                    },
                    {
                        name: "莫利塞 Molise",
                        sub: [{name: "地级市、县"}, {name: "坎波巴索 Campobasso"}],
                        type: 0
                    },
                    {
                        name: "皮埃蒙特 Piemonte",
                        sub: [{name: "地级市、县"}, {name: "都灵 Torino"}],
                        type: 0
                    },
                    {
                        name: "普利亚 Puglia",
                        sub: [{name: "地级市、县"}, {name: "巴里 Bari"}],
                        type: 0
                    },
                    {
                        name: "撒丁* Sardegna",
                        sub: [{name: "地级市、县"}, {name: "卡利亚里 Cagliari"}],
                        type: 0
                    },
                    {
                        name: "西西里* Sicilia",
                        sub: [{name: "地级市、县"}, {name: "巴勒莫 Palermo"}],
                        type: 0
                    },
                    {
                        name: "托斯卡纳 Toscana",
                        sub: [{name: "地级市、县"}, {name: "佛罗伦萨 Firenze"}],
                        type: 0
                    },
                    {
                        name: "特伦蒂诺-上阿迪杰* Trentino-Alto Adige",
                        sub: [{name: "地级市、县"}, {name: "特伦托 Trento"}],
                        type: 0
                    },
                    {
                        name: "翁布里亚 Umbria",
                        sub: [{name: "地级市、县"}, {name: "佩鲁贾 Perugia"}],
                        type: 0
                    },
                    {
                        name: "瓦莱·达奥斯塔* Valle d'Aosta",
                        sub: [{name: "地级市、县"}, {name: "奥斯塔 Aosta"}],
                        type: 0
                    },
                    {
                        name: "威尼托 Veneto",
                        sub: [{name: "地级市、县"}, {name: "威尼斯 Venezia"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "俄罗斯",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "西北 Severo-Zapadnyj",
                        sub: [{name: "地级市、县"}, {name: "阿尔汉格尔斯克州 Archangel'sk Obl."}, {name: "涅涅茨自治区 Nenetskiy AOK"}, {name: "圣彼得堡市 Gorod Sankt-Peterburg"}, {name: "加里宁格勒州 Kaliningrad Obl."}, {name: "卡累利阿共和国 Karelija ARep."}, {name: "科米共和国 Komi ARep."}, {name: "列宁格勒州 Leningrad Obl."}, {name: "摩尔曼斯克州 Murmansk Obl."}, {name: "诺夫哥罗德州 Novgorod Obl."}, {name: "普斯科夫州 Pskov Obl."}, {name: "沃洛格达州 Vologda Obl."}],
                        type: 0
                    },
                    {
                        name: "中央 Central'nyj ",
                        sub: [{name: "地级市、县"}, {name: "别尔哥罗德州 Belgorod Obl."}, {name: "布良斯克州 Br'ansk Obl."}, {name: "莫斯科市 Gorod Moskva."}, {name: "伊万诺沃州 Ivanovo Obl."}, {name: "雅罗斯拉夫尔州 Jaroslavl' Obl."}, {name: "卡卢加州 Kaluga Obl."}, {name: "库尔斯克州 Kursk Obl."}, {name: "莫斯科州 Moskva Obl."}],
                        type: 0
                    },
                    {
                        name: "南方 Juznyj",
                        sub: [{name: "地级市、县"}, {name: "阿迪格共和国 Adygeja ARep."}, {name: "阿斯特拉罕州 Astrachan' Obl."}, {name: "车臣共和国 Cecenija ARep."}, {name: "达吉斯坦共和国 Dagestan  ARep."}, {name: "印古什共和国 Ingusetija ARep."}, {name: "卡巴尔达－巴尔卡尔共和国 Kabardino-Balkarija ARep."}, {name: "卡尔梅克共和国 Kalmykija ARep."}, {name: "卡拉恰耶夫－切尔克斯共和国 Karacajevo-Cerkesija ARep."}, {name: "克拉斯诺达尔边疆区 Krasnodar Kraj."}, {name: "罗斯托夫州 Rostov Obl."}, {name: "北奥塞梯－阿兰社会主义共和国 Severnaja Osetija-Alanija ARep."}, {name: "斯塔夫罗波尔边疆区 Stavropol' Kraj."}, {name: "伏尔加格勒州 Volgograd Obl."}],
                        type: 0
                    },
                    {
                        name: "伏尔加 Privolzskij",
                        sub: [{name: "地级市、县"}, {name: "巴什科尔托斯坦共和国 Ba?kortostan ARep."}, {name: "楚瓦什共和国 ?uva?ija  ARep."}, {name: "基洛夫州 Kirov  Obl."}, {name: "马里－埃尔共和国 Marij El  ARep."}, {name: "莫尔多瓦社会主义共和国 Mordovija  ARep."}, {name: "下诺夫哥罗德州 Niznij Novgorod  Obl."}, {name: "奥伦堡州 Orenburg  Obl."}, {name: "奔萨州 Penza  Obl."}, {name: "彼尔姆州 Perm'  Obl."}, {name: "科米－彼尔米亚克自治区  Komi-Permyatskiy AOK"}, {name: "萨马拉州 Samara  Obl."}, {name: "萨拉托夫州 Saratov  Obl."}],
                        type: 0
                    },
                    {
                        name: "乌拉尔 Ural'skij",
                        sub: [{name: "地级市、县"}, {name: "车里雅宾斯克州 Cel'abinsk Obl."}, {name: "库尔干州 Kurgan Obl."}, {name: "斯维尔德洛夫斯克州 Sverdlovsk Obl."}, {name: "秋明州 T'umen' Obl."}, {name: "汉特－曼西自治区 Khanty-Mansiyskiy AOK"}, {name: "亚马尔－涅涅茨自治区 Yamalo-Nenetskiy AOK"}],
                        type: 0
                    },
                    {
                        name: "西伯利亚 Sibirskij",
                        sub: [{name: "地级市、县"}, {name: "赤塔州 Cita Obl."}, {name: "Чита г. 赤塔市"}, {name: "Балей 巴列伊市"}, {name: "Петровск-Забайкальский г. 外贝加尔的彼得罗夫斯克市"}, {name: "Борзя г. 博尔贾市"},{name:"Краснокаменск г. 克拉斯诺卡缅斯克市"},{name: "Северобайкальск г. 北贝加尔斯克市"},{name: "Улан-Удэ г. 乌兰乌德市"},{name: "Гусиноозерск г. 古西诺奥泽尔斯克市"},{name: "伊尔库茨克州 Irkutsk Obl."},{name: "Усть-Кут г. 乌斯季库特市"},{name: "Бодайбо 博代博市"},{name: "Тайшет г. 泰舍特市"},{name: "Братск г. 布拉茨克市"},{name: "Нижнеудинск г. 下乌金斯克市"},{name: "Тулун 图伦市"},{name: "Саянск 萨彦斯克市"},{name: "特瓦共和国 Tyva ARep."},{name: "克拉斯诺亚尔斯克边疆区 Krasnojarsk ARep."},{name: "哈卡斯共和国 Chakasija ARep."},{name: "阿尔泰共和国 Altaj  ARep."},{name: "阿尔泰边疆区 Altaskij Kraj"},{name: "克麦罗沃州 Kemerovo Obl."},{name: "新西伯利亚州 Novosibirsk Obl."},{name: "托木斯克州 Tomsk Obl."},{name: "鄂木斯克州 Omsk Obl."}],
                        type: 0
                    },
                    {
                        name: "远东 Dal'nevostocnij",
                        sub: [{name: "地级市、县"}, {name: "滨海边疆区 Приморский край/ Primorskij Kraj."}, {name: "哈巴罗夫斯克边疆区 Хабаровский край/ Chabarovsk Kraj."}, {name: "犹太自治州 Еврейская автономная область/Jevrej AArea."}, {name: "阿穆尔州 Amur Obl."}, {name: "萨哈林州 Sakhalin Obl."}, {name: "马加丹州 Magadan Obl."}, {name: "勘察加州 Kamcatka Obl."}, {name: "楚科奇自治专区 Cukotskij Avtonomnyj Okrug AArea."}, {name: "萨哈（雅库特）共和国 Sacha (Jakutija) ARep."}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "荷兰",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "德伦特 Drenthe",
                        sub: [{name: "地级市、县"}, {name: "阿森 Assen"}, {name: "埃门 Emmen"}],
                        type: 0
                    },
                    {
                        name: "弗莱福兰 Flevoland",
                        sub: [{name: "地级市、县"}, {name: "莱利斯塔德 Lelystad"}, {name: "阿尔梅勒 Almere"}],
                        type: 0
                    },
                    {
                        name: "弗里斯兰* Friesland",
                        sub: [{name: "地级市、县"}, {name: "吕伐登 Leeuwarden"}],
                        type: 0
                    },
                    {
                        name: "海尔德兰 Gelderland",
                        sub: [{name: "地级市、县"}, {name: "阿纳姆 Arnhem"}, {name: "阿珀尔多伦 Apeldoorn"}, {name: "埃德 Ede"}, {name: "奈梅亨 Nijmegen"}],
                        type: 0
                    },
                    {
                        name: "格罗宁根 Groningen",
                        sub: [{name: "地级市、县"}, {name: "格罗宁根 Groningen"}],
                        type: 0
                    },
                    {
                        name: "林堡 Limburg",
                        sub: [{name: "地级市、县"}, {name: "马斯特里赫特 Maastricht"}],
                        type: 0
                    },
                    {
                        name: "北布拉班特 Noord-Brabant",
                        sub: [{name: "地级市、县"}, {name: "斯海尔托亨博思 's-Hertogenbosch"}, {name: "布雷达 Breda"}, {name: "艾恩德霍芬 Eindhoven"}, {name: "蒂尔堡 Tilburg"}],
                        type: 0
                    },
                    {
                        name: "北荷兰 Noord-Holland",
                        sub: [{name: "地级市、县"}, {name: "哈勒姆 Haarlem"}, {name: "阿姆斯特丹 Amsterdam"}, {name: "赞济科 Zaandijk"}, {name: "霍夫多尔普 Hoofddorp"}],
                        type: 0
                    },
                    {
                        name: "上艾瑟尔 Overijssel",
                        sub: [{name: "地级市、县"}, {name: "兹沃勒 Zwolle"}, {name: "恩斯赫德 Enschede"}],
                        type: 0
                    },
                    {
                        name: "乌得勒支 Utrecht",
                        sub: [{name: "地级市、县"}, {name: "乌得勒支 Utrecht"}, {name: "阿默斯福特 Amersfoort"}],
                        type: 0
                    },
                    {
                        name: "泽兰 Zeeland",
                        sub: [{name: "地级市、县"}, {name: "米德尔堡 Middelburg"}],
                        type: 0
                    },
                    {
                        name: "南荷兰 Zuid-Holland",
                        sub: [{name: "地级市、县"}, {name: "海牙 's-Gravenhage"}, {name: "鹿特丹 Rotterdam"}, {name: "多德雷赫特 Dordrecht"}, {name: "莱顿 Leiden"}, {name: "佐特尔梅 Zoetermeer"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "美国",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "阿拉巴马 Alabama",
                        sub: [{name: "地级市、县"}, {name: "蒙哥马利 Montgomery"}],
                        type: 0
                    },
                    {
                        name: "阿拉斯加 Alaska",
                        sub: [{name: "地级市、县"}, {name: "朱诺 Juneau"}],
                        type: 0
                    },
                    {
                        name: "亚利桑那 Arizona",
                        sub: [{name: "地级市、县"}, {name: "菲尼克斯 Phoenix"}],
                        type: 0
                    },
                    {
                        name: "阿肯色 Arkansas",
                        sub: [{name: "地级市、县"}, {name: "小石城 Little Rock"}],
                        type: 0
                    },
                    {
                        name: "加利福尼亚 California",
                        sub: [{name: "地级市、县"}, {name: "萨克拉门多 Sacrament"}],
                        type: 0
                    },
                    {
                        name: "科罗拉多 Colorado",
                        sub: [{name: "地级市、县"}, {name: "丹佛 Denver"}],
                        type: 0
                    },
                    {
                        name: "康涅狄格 Connecticut",
                        sub: [{name: "地级市、县"}, {name: "哈特福德 Hartford"}],
                        type: 0
                    },
                    {
                        name: "特拉华 Delaware",
                        sub: [{name: "地级市、县"}, {name: "多佛 Dover"}],
                        type: 0
                    },
                    {
                        name: "哥伦比亚特区 District of Columbia",
                        sub: [{name: "地级市、县"}, {name: "华盛顿 Washington"}],
                        type: 0
                    },
                    {
                        name: "佛罗里达 Florida",
                        sub: [{name: "地级市、县"}, {name: "塔拉哈西 Tallahassee"}],
                        type: 0
                    },
                    {
                        name: "乔治亚 Georgia",
                        sub: [{name: "地级市、县"}, {name: "亚特兰大 Atlanta"}],
                        type: 0
                    },
                    {
                        name: "夏威夷 Hawaii",
                        sub: [{name: "地级市、县"}, {name: "檀香山 Honolulu"}],
                        type: 0
                    },
                    {
                        name: "伊利诺斯 Illinois",
                        sub: [{name: "地级市、县"}, {name: "博伊亚 Boise"}],
                        type: 0
                    },
                    {
                        name: "印地安那 Indiana",
                        sub: [{name: "地级市、县"}, {name: "斯普林菲尔德 Springfield"}],
                        type: 0
                    },
                    {
                        name: "衣阿华 Iowa",
                        sub: [{name: "地级市、县"}, {name: "印第安纳波利斯 Indianapolis"}],
                        type: 0
                    },
                    {
                        name: "堪萨斯 Kansas",
                        sub: [{name: "地级市、县"}, {name: "得梅因 Des Moines"}],
                        type: 0
                    },
                    {
                        name: "肯塔基 Kentucky",
                        sub: [{name: "地级市、县"}, {name: "托皮卡 Topeka"}],
                        type: 0
                    },
                    {
                        name: "路易斯安那 Louisiana",
                        sub: [{name: "地级市、县"}, {name: "法兰克福 Frankfort"}],
                        type: 0
                    },
                    {
                        name: "缅因 Maine",
                        sub: [{name: "地级市、县"}, {name: "奥古斯塔 Augusta"}],
                        type: 0
                    },
                    {
                        name: "马里兰 Maryland",
                        sub: [{name: "地级市、县"}, {name: "安纳波利斯 Annapolis"}],
                        type: 0
                    },
                    {
                        name: "马萨诸塞 Massachusetts",
                        sub: [{name: "地级市、县"}, {name: "波土顿 Boston"}],
                        type: 0
                    },
                    {
                        name: "密歇根 Michigan",
                        sub: [{name: "地级市、县"}, {name: "兰辛 Lansing"}],
                        type: 0
                    },
                    {
                        name: "明尼苏达 Minnesota",
                        sub: [{name: "地级市、县"}, {name: "圣保罗 St.Paul"}],
                        type: 0
                    },
                    {
                        name: "密西西比 Mississippi",
                        sub: [{name: "地级市、县"}, {name: "杰克逊 Jackson"}],
                        type: 0
                    },
                    {
                        name: "密苏里 Missouri",
                        sub: [{name: "地级市、县"}, {name: "杰斐逊城 Jefferson City"}],
                        type: 0
                    },
                    {
                        name: "蒙大拿 Montana",
                        sub: [{name: "地级市、县"}, {name: "赫勒纳 Helena"}],
                        type: 0
                    },
                    {
                        name: "内布拉斯加 Nebraska",
                        sub: [{name: "地级市、县"}, {name: "林肯 Lincoln"}],
                        type: 0
                    },
                    {
                        name: "内华达 Nevada",
                        sub: [{name: "地级市、县"}, {name: "卡森城 Carson City"}],
                        type: 0
                    },
                    {
                        name: "新罕布什尔 New Hampshire",
                        sub: [{name: "地级市、县"}, {name: "康科德 Concord"}],
                        type: 0
                    },
                    {
                        name: "新泽西 New Jersey",
                        sub: [{name: "地级市、县"}, {name: "特伦顿 Trenton"}],
                        type: 0
                    },
                    {
                        name: "新墨西哥 New Mexico",
                        sub: [{name: "地级市、县"}, {name: "圣菲 Santa Fe"}],
                        type: 0
                    },
                    {
                        name: "纽约 New York",
                        sub: [{name: "地级市、县"}, {name: "奥尔巴尼 Albany"}],
                        type: 0
                    },
                    {
                        name: "犹他 Utah",
                        sub: [{name: "地级市、县"}, {name: "盐湖城 Salt Lake City"}],
                        type: 0
                    },
                    {
                        name: "华盛顿 Washington",
                        sub: [{name: "地级市、县"}, {name: "奥林匹亚 Olympia"}],
                        type: 0
                    },
                    {
                        name: "威斯康星 Wisconsin",
                        sub: [{name: "地级市、县"}, {name: "麦迪逊 Madison"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "加拿大",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "新不伦瑞克省 New Brunswick",
                        sub: [{name: "地级市、县"}, {name: "弗雷德里顿 Fredericton"}],
                        type: 0
                    },
                    {
                        name: "新斯科舍省 Nova Scotia",
                        sub: [{name: "地级市、县"}, {name: "哈利法克斯 Halifax"}, {name: "布列塔尼角 Cape Breton"}],
                        type: 0
                    },
                    {
                        name: "安大略省 Ontario",
                        sub: [{name: "地级市、县"}, {name: "多伦多 Toronto"}, {name: "渥太华 Ottawa"}, {name: "哈密尔顿 Hamilton"}, {name: "基奇纳 Kitchener"}, {name: "伦敦 London"}, {name: "圣卡塔琳娜 St. Catharines"}, {name: "温莎 Windsor"}, {name: "奥沙瓦 Oshawa"}, {name: "巴里 Barrie"}, {name: "金斯敦 Kingston"}, {name: "圭尔夫 Guelph"}, {name: "萨德伯里 Sudbury"}, {name: "桑德贝 Thunder Bay"}],
                        type: 0
                    },
                    {
                        name: "魁北克省 Québec",
                        sub: [{name: "地级市、县"}, {name: "魁北克 Québec"}, {name: "蒙特利尔 Montréal"}, {name: "舍布鲁克 Sherbrooke"}, {name: "钻石城 Trois-Rivières"}, {name: "希格蒂米 Chicoutimi"}],
                        type: 0
                    },
                    {
                        name: "马尼托巴省 Manitoba",
                        sub: [{name: "地级市、县"}, {name: "温尼伯 Winnipeg"}],
                        type: 0
                    },
                    {
                        name: "不列颠哥伦比亚省 British Columbia",
                        sub: [{name: "地级市、县"}, {name: "维多利亚 Victoria"}, {name: "温哥华 Vancouver"}, {name: "阿伯茨福 Abbotsford"}, {name: "基劳纳 Kelowna"}],
                        type: 0
                    },
                    {
                        name: "爱德华王子岛省 Prince Edward Island",
                        sub: [{name: "地级市、县"}, {name: "夏洛特敦 Charlottetown"}],
                        type: 0
                    },
                    {
                        name: "艾伯塔省 Alberta",
                        sub: [{name: "地级市、县"}, {name: "埃德蒙顿 Edmonton"}, {name: "卡里加里 Calgary"}],
                        type: 0
                    },
                    {
                        name: "萨斯喀彻温省 Saskatchewan",
                        sub: [{name: "地级市、县"}, {name: "里贾纳 Regina"}, {name: "萨斯卡通 Saskatoon"}],
                        type: 0
                    },
                    {
                        name: "纽芬兰-拉布拉多省 Newfoundland-Labrador",
                        sub: [{name: "地级市、县"}, {name: "圣约翰斯 Saint-John's"}],
                        type: 0
                    },
                    {
                        name: "西北地区 Northwest Territories",
                        sub: [{name: "地级市、县"}, {name: "耶洛奈夫 Yellowknife"}],
                        type: 0
                    },
                    {
                        name: "育空地区 Yukon Territory",
                        sub: [{name: "地级市、县"}, {name: "怀特霍斯 Whitehorse"}],
                        type: 0
                    },
                    {
                        name: "努纳维特地区 Nunavut Territory",
                        sub: [{name: "地级市、县"}, {name: "伊魁特 Iqaluit"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "巴西",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "联邦首都 Distrito Federal",
                        sub: [{name: "地级市、县"}, {name: "巴西利亚 Brasília"}],
                        type: 0
                    },
                    {
                        name: "戈亚斯 Goiás",
                        sub: [{name: "地级市、县"}, {name: "戈亚尼亚 Goiania"}],
                        type: 0
                    },
                    {
                        name: "马托格罗索 Mato Grosso",
                        sub: [{name: "地级市、县"}, {name: "库亚巴 Cuiabá"}],
                        type: 0
                    },
                    {
                        name: "南马托格罗索 Mato Grosso do Sul",
                        sub: [{name: "地级市、县"}, {name: "大坎普 Campo Grande"}],
                        type: 0
                    },
                    {
                        name: "阿拉戈斯 Alagoas",
                        sub: [{name: "地级市、县"}, {name: "马塞约 Maceió"}],
                        type: 0
                    },
                    {
                        name: "巴伊亚 Bahia",
                        sub: [{name: "地级市、县"}, {name: "萨尔瓦多 Salvador"}],
                        type: 0
                    },
                    {
                        name: "塞阿拉 Ceará",
                        sub: [{name: "地级市、县"}, {name: "福塔莱萨 Fortaleza"}],
                        type: 0
                    },
                    {
                        name: "马拉尼昂 Maranhao",
                        sub: [{name: "地级市、县"}, {name: "圣路易斯 Sao Luís"}],
                        type: 0
                    },
                    {
                        name: "帕拉伊巴 Paraíba",
                        sub: [{name: "地级市、县"}, {name: "若昂佩索阿 Joao Pessoa"}],
                        type: 0
                    },
                    {
                        name: "伯南布哥 Pernambuco",
                        sub: [{name: "地级市、县"}, {name: "累西腓 Recife"}],
                        type: 0
                    },
                    {
                        name: "皮奥伊 Piauí",
                        sub: [{name: "地级市、县"}, {name: "特雷西纳 Teresina"}],
                        type: 0
                    },
                    {
                        name: "北里奥格兰德 Rio Grande do Norte",
                        sub: [{name: "地级市、县"}, {name: "纳塔尔 Natal"}],
                        type: 0
                    },
                    {
                        name: "塞尔希培 Sergipe",
                        sub: [{name: "地级市、县"}, {name: "阿拉卡茹 Aracaju"}],
                        type: 0
                    },
                    {
                        name: "阿克里 Acre",
                        sub: [{name: "地级市、县"}, {name: "里奥布朗库 Rio Branco"}],
                        type: 0
                    },
                    {
                        name: "阿马帕 Amapá",
                        sub: [{name: "地级市、县"}, {name: "马卡帕 Macapá"}],
                        type: 0
                    },
                    {
                        name: "亚马孙 Amazonas",
                        sub: [{name: "地级市、县"}, {name: "马瑙斯 Manaus"}],
                        type: 0
                    },
                    {
                        name: "帕拉 Pará",
                        sub: [{name: "地级市、县"}, {name: "贝伦 Belém"}],
                        type: 0
                    },
                    {
                        name: "朗多尼亚 Rondonia",
                        sub: [{name: "地级市、县"}, {name: "波多韦柳 Porto Velho"}],
                        type: 0
                    },
                    {
                        name: "罗赖马 Roraima",
                        sub: [{name: "地级市、县"}, {name: "沃阿维斯塔 Boa Vista"}],
                        type: 0
                    },
                    {
                        name: "托坎廷斯 Tocantins",
                        sub: [{name: "地级市、县"}, {name: "帕尔马斯 Palmas"}],
                        type: 0
                    },
                    {
                        name: "圣埃斯皮里图 Espírito Santo*",
                        sub: [{name: "地级市、县"}, {name: "维多利亚 Vitória"}],
                        type: 0
                    },
                    {
                        name: "米纳斯吉拉斯 Minas Gerais",
                        sub: [{name: "地级市、县"}, {name: "贝洛奥里藏特 Belo Horizonte"}],
                        type: 0
                    },
                    {
                        name: "里约热内卢 Rio de Janeiro",
                        sub: [{name: "地级市、县"}, {name: "里约热内卢 Rio de Janeiro"}],
                        type: 0
                    },
                    {
                        name: "圣保罗 Sao Paulo",
                        sub: [{name: "地级市、县"}, {name: "圣保罗 Sao Paulo"}],
                        type: 0
                    },
                    {
                        name: "巴拉那 Paraná",
                        sub: [{name: "地级市、县"}, {name: "库里蒂巴 Curitiba"}],
                        type: 0
                    },
                    {
                        name: "南里奥格兰德 Rio Grande do Sul",
                        sub: [{name: "地级市、县"}, {name: "阿雷格里港 Porto Alegre"}],
                        type: 0
                    },
                    {
                        name: "圣卡塔琳娜 Santa Catarina",
                        sub: [{name: "地级市、县"}, {name: "弗洛里亚诺波利斯 Florianópolis"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "阿根廷",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "联邦首都 Distrito Federal",
                        sub: [{name: "地级市、县"}, {name: "布宜诺斯艾利斯  Buenos Aires"}],
                        type: 0
                    },
                    {
                        name: "布宜诺斯艾利斯 Buenos Aires",
                        sub: [{name: "地级市、县"}, {name: "拉普拉塔 La Plata"}, {name: "布兰卡港 Bahía Blanca"}, {name: "马德普拉塔 Mar del Plata"}, {name: "圣尼古拉斯 San Nic+olás"}],
                        type: 0
                    },
                    {
                        name: "卡塔马卡 Catamarca",
                        sub: [{name: "地级市、县"}, {name: "卡塔马卡 Catamarca"}],
                        type: 0
                    },
                    {
                        name: "查科 Chaco",
                        sub: [{name: "地级市、县"}, {name: "雷西斯滕匹亚　Resistencia"}],
                        type: 0
                    },
                    {
                        name: "丘布特 Chubut",
                        sub: [{name: "地级市、县"}, {name: "罗森 Rawson"}, {name: "特雷利乌Trelew"}, {name: "里瓦达维亚海军准将城 Comodoro Rivadavia"}],
                        type: 0
                    },
                    {
                        name: "科尔多瓦  Córdoba",
                        sub: [{name: "地级市、县"}, {name: "科尔多瓦 Córdoba"}, {name: "里奥夸尔托 Río Cuarto"}],
                        type: 0
                    },
                    {
                        name: "科连特斯 Corrientes",
                        sub: [{name: "地级市、县"}, {name: "科连特斯 Corrientes"}],
                        type: 0
                    },
                    {
                        name: "恩特雷里奥斯 Entre Ríos",
                        sub: [{name: "地级市、县"}, {name: "巴拉那　Paraná"}, {name: "肯考迪娅 Concordia"}],
                        type: 0
                    },
                    {
                        name: "福莫萨 Formosa",
                        sub: [{name: "地级市、县"}, {name: "福莫萨　Formosa"}],
                        type: 0
                    },
                    {
                        name: "胡胡伊 Jujuy",
                        sub: [{name: "地级市、县"}, {name: "胡胡伊 Jujuy"}],
                        type: 0
                    },
                    {
                        name: "拉潘帕 La Pampa",
                        sub: [{name: "地级市、县"}, {name: "圣罗莎　Santa Rosa"}],
                        type: 0
                    },
                    {
                        name: "拉里奥哈 La Rioja",
                        sub: [{name: "地级市、县"}, {name: "拉里奥哈　La Rioja"}],
                        type: 0
                    },
                    {
                        name: "门多萨　Mendoza",
                        sub: [{name: "地级市、县"}, {name: "门多萨 Mendoza"}, {name: "圣拉斐尔 San Rafael"}],
                        type: 0
                    },
                    {
                        name: "米西奥斯内斯　Misiones",
                        sub: [{name: "地级市、县"}, {name: "波萨达斯　Posadas"}],
                        type: 0
                    },
                    {
                        name: "内乌肯　Neuquén",
                        sub: [{name: "地级市、县"}, {name: "内乌肯　Neuquén"}],
                        type: 0
                    },
                    {
                        name: "里奥内格罗 Río Negro",
                        sub: [{name: "地级市、县"}, {name: "别德马　Viedma"}],
                        type: 0
                    },
                    {
                        name: "萨尔塔　Salta",
                        sub: [{name: "地级市、县"}, {name: "萨尔塔　Salta"}],
                        type: 0
                    },
                    {
                        name: "圣胡安　San Juan",
                        sub: [{name: "地级市、县"}, {name: "圣胡安　San Juan"}, {name: "克劳斯城 Villa Krause (Rawson)"}, {name: "圣路易斯 San Luis"}],
                        type: 0
                    },
                    {
                        name: "圣路易斯　San Luis",
                        sub: [{name: "地级市、县"}, {name: "圣路易斯　San Luis"}],
                        type: 0
                    },
                    {
                        name: "圣克鲁斯　Santa Cruz",
                        sub: [{name: "地级市、县"}, {name: "里奥加耶戈斯　Río Gallegos"}],
                        type: 0
                    },
                    {
                        name: "圣菲　Santa Fe",
                        sub: [{name: "地级市、县"}, {name: "圣菲　Santa Fe"}, {name: "罗萨里奥 Rosario"}],
                        type: 0
                    },
                    {
                        name: "圣地亚哥-德尔埃斯特罗 Santiago del Estero",
                        sub: [{name: "地级市、县"}, {name: "圣地亚哥-德尔埃斯特罗 Santiago del Estero"}],
                        type: 0
                    },
                    {
                        name: "火地岛　Tierra del Fuego",
                        sub: [{name: "地级市、县"}, {name: "乌斯怀亚　Ushuaia"}],
                        type: 0
                    },
                    {
                        name: "图库曼　Tucumán",
                        sub: [{name: "地级市、县"}, {name: "圣米格尔-德图库曼 San Miguel de Tucumán"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "新西兰",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "北地 Northland",
                        sub: [{name: "地级市、县"}, {name: "旺阿雷 Whangarei"}, {name: "北远 Far North"}, {name: "凯帕拉 Kaipara"}],
                        type: 0
                    },
                    {
                        name: "奥克兰 Auckland",
                        sub: [{name: "地级市、县"}, {name: "奥克兰 Auckland"}, {name: "马努考 Manukau"}, {name: "北岸 North Shore"}, {name: "怀塔科拉 Waitakere"}, {name: "罗得尼 Rodney"}, {name: "帕帕库拉 Papakura"}, {name: "富兰克林 Franklin (1)"}],
                        type: 0
                    },
                    {
                        name: "怀卡托 Waikato",
                        sub: [{name: "地级市、县"}, {name: "哈密尔顿  Hamilton"}, {name: "怀卡托 Waikato"}, {name: "怀帕 Waipa"}, {name: "Otorohanga"}, {name: "Waitomo (7)"}, {name: "Thames-Coromandel"}, {name: "Hauraki"}],
                        type: 0
                    },
                    {
                        name: "普伦蒂湾 Bay of Plenty",
                        sub: [{name: "地级市、县"}, {name: "Tauranga"}, {name: "Western Bay op Plenty"}, {name: "Rotorua (2)"}, {name: "Taupo (3)"}, {name: "瓦卡塔尼 Whakatane"}, {name: "Kawerau"}, {name: "Opotiki"}],
                        type: 0
                    },
                    {
                        name: "吉斯伯恩 Gisborne (A) ",
                        sub: [{name: "地级市、县"}, {name: "吉斯伯恩 Gisborne"}],
                        type: 0
                    },
                    {
                        name: "霍克湾 Hawkes Bay",
                        sub: [{name: "地级市、县"}, {name: "内皮尔 Napier"}, {name: "Wairoa"}, {name: "Taupo (3)"}, {name: "Hastings"}, {name: "Rangitikei (4)"}, {name: "Central Hawke's Bay"}],
                        type: 0
                    },
                    {
                        name: "玛纳瓦图/旺格努伊 Manawatu-Wanganui",
                        sub: [{name: "地级市、县"}, {name: "北帕默斯顿 Palmerston North"}, {name: "Tararua (6)"}, {name: "Horowhenua"}, {name: "Manawatu"}, {name: "Rangitikei (4)"}, {name: "Ruapehu"}, {name: "Wanganui"}, {name: "斯特拉特福德 Stratford (5)"}],
                        type: 0
                    },
                    {
                        name: "塔拉那基 Taranaki",
                        sub: [{name: "地级市、县"}, {name: "新普利茅斯 New Plymouth"}, {name: "斯特拉特福德 Stratford (5)"}, {name: "南塔拉纳基 South Taranaki"}],
                        type: 0
                    },
                    {
                        name: "惠灵顿 Wellington",
                        sub: [{name: "地级市、县"}, {name: "Wellington"}, {name: "Lower Hutt ( Hutt )"}, {name: "Porirua"}, {name: "Upper Hutt"}, {name: "Kapiti Coast"}, {name: "Masterton"}, {name: "Carterton"}, {name: "South Wairarapa"}],
                        type: 0
                    },
                    {
                        name: "塔斯曼 Tasman (A)",
                        sub: [{name: "地级市、县"}, {name: "里士满 Richmond"}],
                        type: 0
                    },
                    {
                        name: "纳尔逊 Nelson (B)",
                        sub: [{name: "地级市、县"}, {name: "纳尔逊  Nelson"}],
                        type: 0
                    },
                    {
                        name: "马尔伯勒 Blenheim (A)",
                        sub: [{name: "地级市、县"}, {name: "布莱尼姆  Blenheim"}],
                        type: 0
                    },
                    {
                        name: "西岸 West Coast",
                        sub: [{name: "地级市、县"}, {name: "格雷茅斯 Greymouth"}, {name: "Buller"}, {name: "格雷 Grey"}, {name: "西地 Westland"}],
                        type: 0
                    },
                    {
                        name: "坎特伯雷 Canterbury",
                        sub: [{name: "地级市、县"}, {name: "基督城 Christchurch"}, {name: "Kaikoura"}, {name: "Hurunui"}, {name: "班克斯半岛 Banks Peninsula"}, {name: "塞尔温 Selwyn"}],
                        type: 0
                    },
                    {
                        name: "奥塔戈 Otago",
                        sub: [{name: "地级市、县"}, {name: "达尼丁 Dunedin"}, {name: "中奥塔戈 Central Otago"}, {name: "Queenstown-Lakes"}],
                        type: 0
                    },
                    {
                        name: "南地 Southland",
                        sub: [{name: "地级市、县"}, {name: "因弗卡吉尔 Invercargill"}, {name: "Gore"}, {name: "南地 Southland"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "澳大利亚",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "新南威尔士州 New South Wales",
                        sub: [{name: "地级市、县"}, {name: "悉尼 Sydney"}, {name: "伍伦贡 Wollongong"}, {name: "纽卡斯尔 Newcastle"}],
                        type: 0
                    },
                    {
                        name: "昆士兰州 Queensland",
                        sub: [{name: "地级市、县"}, {name: "布里斯班 Brisbane"}, {name: "黄金海岸 Gold Coast"}, {name: "日光海岸 Caloundra"}, {name: "汤斯维尔 Townsville"}, {name: "凯恩斯 Cairns"}, {name: "图文巴 Toowoomba"}],
                        type: 0
                    },
                    {
                        name: "南澳大利亚州 South Australia",
                        sub: [{name: "地级市、县"}, {name: "阿德莱德 Adelaide"}],
                        type: 0
                    },
                    {
                        name: "塔斯马尼亚州 Tasmania",
                        sub: [{name: "地级市、县"}, {name: "霍巴特 Hobart"}],
                        type: 0
                    },
                    {
                        name: "维多利亚州 Victoria",
                        sub: [{name: "地级市、县"}, {name: "墨尔本 Melbourne"}, {name: "吉朗 Geelong"}],
                        type: 0
                    },
                    {
                        name: "西澳大利亚州 Western Australia",
                        sub: [{name: "地级市、县"}, {name: "珀斯 Perth"}],
                        type: 0
                    },
                    {
                        name: "澳大利亚首都地区 Australian Capital Territory",
                        sub: [{name: "地级市、县"}, {name: "堪培拉 Canberra"}],
                        type: 0
                    },
                    {
                        name: "北部地区 Northern Territory",
                        sub: [{name: "地级市、县"}, {name: "达尔文 Darwin"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "印度",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "查谟和克什米尔* Jammu & Kashmīr",
                        sub: [{name: "地级市、县"}, {name: "斯利那加 Srinagar"}],
                        type: 0
                    },
                    {
                        name: "旁遮普 Punjub",
                        sub: [{name: "地级市、县"}, {name: "昌迪加尔 Chandigarh"}],
                        type: 0
                    },
                    {
                        name: "昌迪加尔 Chandīgarh",
                        sub: [{name: "地级市、县"}, {name: "昌迪加尔 Chandigarh"}],
                        type: 0
                    },
                    {
                        name: "喜马偕尔邦 Himāchal Pradesh",
                        sub: [{name: "地级市、县"}, {name: "西姆拉 Simla"}],
                        type: 0
                    },
                    {
                        name: "北安查尔 Uttaranchal",
                        sub: [{name: "地级市、县"}, {name: "德拉敦 Dehra Dun"}],
                        type: 0
                    },
                    {
                        name: "哈里亚纳 Haryāna",
                        sub: [{name: "地级市、县"}, {name: "昌迪加尔 Chandigarh"}],
                        type: 0
                    },
                    {
                        name: "德里 Delhi",
                        sub: [{name: "地级市、县"}, {name: "德里 Delhi"}],
                        type: 0
                    },
                    {
                        name: "拉贾斯坦 Rājasthān",
                        sub: [{name: "地级市、县"}, {name: "斋浦尔 Jaipur"}],
                        type: 0
                    },
                    {
                        name: "北方邦 Uttar Pradesh",
                        sub: [{name: "地级市、县"}, {name: "勒克瑙 Lucknow"}],
                        type: 0
                    },
                    {
                        name: "中央邦 Madhya Pradesh",
                        sub: [{name: "地级市、县"}, {name: "博帕尔 Bhopal"}],
                        type: 0
                    },
                    {
                        name: "查蒂斯加尔 Chhatisgarh",
                        sub: [{name: "地级市、县"}, {name: "赖布尔 Raipur"}],
                        type: 0
                    },
                    {
                        name: "比哈尔 Bihār",
                        sub: [{name: "地级市、县"}, {name: "巴特那 Patna"}],
                        type: 0
                    },
                    {
                        name: "贾坎德 Jharkhand",
                        sub: [{name: "地级市、县"}, {name: "兰契 Ranchi"}],
                        type: 0
                    },
                    {
                        name: "锡金 Sikkim",
                        sub: [{name: "地级市、县"}, {name: "甘托克 Gangtok"}],
                        type: 0
                    },
                    {
                        name: "阿鲁那恰尔邦* Arunāchal Pradesh",
                        sub: [{name: "地级市、县"}, {name: "伊塔那噶 Itanagar"}],
                        type: 0
                    },
                    {
                        name: "那加兰 Nāgāland",
                        sub: [{name: "地级市、县"}, {name: "科希马 Kohima"}],
                        type: 0
                    },
                    {
                        name: "曼尼普尔 Manipur",
                        sub: [{name: "地级市、县"}, {name: "因帕尔 Imphal"}],
                        type: 0
                    },
                    {
                        name: "米佐拉姆 Mizorām",
                        sub: [{name: "地级市、县"}, {name: "艾藻尔 Aizawl"}],
                        type: 0
                    },
                    {
                        name: "特里普拉 Tripura",
                        sub: [{name: "地级市、县"}, {name: "阿加尔塔拉 Agartala"}],
                        type: 0
                    },
                    {
                        name: "梅加拉亚  Meghālaya",
                        sub: [{name: "地级市、县"}, {name: "西隆 Shillong"}],
                        type: 0
                    },
                    {
                        name: "阿萨姆 Assam",
                        sub: [{name: "地级市、县"}, {name: "迪斯布尔 Dispur"}],
                        type: 0
                    },
                    {
                        name: "西孟加拉邦 West Bengal",
                        sub: [{name: "地级市、县"}, {name: "加尔各答 Kolkata"}],
                        type: 0
                    },
                    {
                        name: "奥里萨 Orissa",
                        sub: [{name: "地级市、县"}, {name: "布巴内斯瓦尔 Bhubaneswar"}],
                        type: 0
                    },
                    {
                        name: "古吉拉特 Gujarāt",
                        sub: [{name: "地级市、县"}, {name: "甘地讷格尔 Gandhinagar"}],
                        type: 0
                    },
                    {
                        name: "达曼和第乌 Damān & Diu",
                        sub: [{name: "地级市、县"}, {name: "达曼 Daman"}],
                        type: 0
                    },
                    {
                        name: "达德拉和纳加尔哈维利 Dādra & Nagar Haveli",
                        sub: [{name: "地级市、县"}, {name: "锡尔瓦萨 Silvassa"}],
                        type: 0
                    },
                    {
                        name: "马哈拉施特拉 Mahārāshtra",
                        sub: [{name: "地级市、县"}, {name: "孟买 Mumbai"}],
                        type: 0
                    },
                    {
                        name: "果阿 Goa",
                        sub: [{name: "地级市、县"}, {name: "帕那吉 Panaji"}],
                        type: 0
                    },
                    {
                        name: "安得拉邦 Andhra Pradesh",
                        sub: [{name: "地级市、县"}, {name: "海得拉巴 Hyderabad"}],
                        type: 0
                    },
                    {
                        name: "卡纳塔克 Karnātaka",
                        sub: [{name: "地级市、县"}, {name: "班加罗尔 Bangalore"}],
                        type: 0
                    },
                    {
                        name: "拉克沙群岛 Lakshadweep",
                        sub: [{name: "地级市、县"}, {name: "卡瓦拉蒂 Kavaratti"}],
                        type: 0
                    },
                    {
                        name: "喀拉拉 Kerala",
                        sub: [{name: "地级市、县"}, {name: "特里凡得琅 Thiruvananthapuram"}],
                        type: 0
                    },
                    {
                        name: "泰米尔纳德 Tamil Nādu",
                        sub: [{name: "地级市、县"}, {name: "金奈 Chennai"}],
                        type: 0
                    },
                    {
                        name: "本地治里 Pondicherry",
                        sub: [{name: "地级市、县"}, {name: "本地治里 Pondicherry"}],
                        type: 0
                    },
                    {
                        name: "安达曼和尼科巴群岛 Andaman & Nicobar Islands",
                        sub: [{name: "地级市、县"}, {name: "布莱尔港 Port Blair"}],
                        type: 0
                    }],
                type: 1
            },
            {
                name: "埃及",
                sub: [{name: "省份、州", sub: []},
                    {
                        name: "开罗 Al Qahirah",
                        sub: [{name: "地级市、县"}, {name: "开罗 Al Qahirah"}],
                        type: 0
                    },
                    {
                        name: "亚历山大 Al Iskandariyah",
                        sub: [{name: "地级市、县"}, {name: "亚历山大 Al Iskandariyah"}],
                        type: 0
                    },
                    {
                        name: "塞得港 Bur Sa`id",
                        sub: [{name: "地级市、县"}, {name: "塞得港 Bur Sa`id"}],
                        type: 0
                    },
                    {
                        name: "苏伊士 As Suways",
                        sub: [{name: "地级市、县"}, {name: "苏伊士 As Suways"}],
                        type: 0
                    },
                    {
                        name: "卢克索 Al Uqsur",
                        sub: [{name: "地级市、县"}, {name: "卢克索 Al Uqsur"}],
                        type: 0
                    },
                    {
                        name: "代盖赫利耶 Ad Daqahl?yah",
                        sub: [{name: "地级市、县"}, {name: "曼苏拉 Al Mansurah"},{name:"米特加穆尔 Mit Ghamr"}],
                        type: 0
                    },
                    {
                        name: "布海拉 Al Buhayrah",
                        sub: [{name: "地级市、县"}, {name: "达曼胡尔 Damanhur"},{name:"达沃 Kafr ad-Dawwar"}],
                        type: 0
                    },
                    {
                        name: "西部 Al Gharbiyah",
                        sub: [{name: "地级市、县"}, {name: "坦塔 Tanta"},{name:"马哈拉库布拉 Al-Mahallah al-Kubra"}],
                        type: 0
                    },
                    {
                        name: "伊斯梅利亚 Al Isma`iliyah",
                        sub: [{name: "地级市、县"}, {name: "伊斯梅利亚 Al Isma`iliyah"}],
                        type: 0
                    },
                    {
                        name: "米努夫 Al Minufiyah",
                        sub: [{name: "地级市、县"}, {name: "希宾库姆 Shibin al Kawm"}],
                        type: 0
                    },
                    {
                        name: "盖勒尤卜 Al Qalyubiyah",
                        sub: [{name: "地级市、县"}, {name: "本哈 Banha"},{name:"苏布拉开马 Shubra al-Khaymah"}],
                        type: 0
                    },
                    {
                        name: "东部 Ash Sharqiyah",
                        sub: [{name: "地级市、县"}, {name: "宰加济格 Az Zaqaziq"},{name:"比勒拜斯 Bilbays"}],
                        type: 0
                    },
                    {
                        name: "杜姆亚特 Dumyat",
                        sub: [{name: "地级市、县"}, {name: "杜姆亚特 Dumyat"}],
                        type: 0
                    },
                    {
                        name: "谢赫村 Kafr ash Shaykh",
                        sub: [{name: "地级市、县"}, {name: "谢赫村 Kafr ash Shaykh"}],
                        type: 0
                    },
                    {
                        name: "吉萨 Al Jizah",
                        sub: [{name: "地级市、县"}, {name: "吉萨 Al Jizah"}],
                        type: 0
                    },
                    {
                        name: "明亚 Al Minya",
                        sub: [{name: "地级市、县"}, {name: "明亚 Al Minya"},{name:"迈莱维 Mallawi"}],
                        type: 0
                    },
                    {
                        name: "贝尼苏韦夫 Bani Suwayf",
                        sub: [{name: "地级市、县"}, {name: "贝尼苏韦夫 Bani Suwayf"}],
                        type: 0
                    },
                    {
                        name: "法尤姆 Al Fayyum",
                        sub: [{name: "地级市、县"}, {name: "法尤姆 Al Fayyum"}],
                        type: 0
                    },
                    {
                        name: "艾斯尤特 Asyut",
                        sub: [{name: "地级市、县"}, {name: "艾斯尤特 Asyut"}],
                        type: 0
                    },
                    {
                        name: "阿斯旺 Aswan",
                        sub: [{name: "地级市、县"}, {name: "阿斯旺 Aswan"}],
                        type: 0
                    },
                    {
                        name: "索哈杰 Suhaj",
                        sub: [{name: "地级市、县"}, {name: "索哈杰 Suhaj"}],
                        type: 0
                    },
                    {
                        name: "基纳 Qina",
                        sub: [{name: "地级市、县"}, {name: "基纳 Qina"}],
                        type: 0
                    },
                    {
                        name: "红海 Al Bahr al Ahmar",
                        sub: [{name: "地级市、县"}, {name: "古尔代盖 Al Ghurdaqah"}],
                        type: 0
                    },
                    {
                        name: "新河谷 Al Wadi al Jadid",
                        sub: [{name: "地级市、县"}, {name: "哈里杰 Al Kharijah"}],
                        type: 0
                    },
                    {
                        name: "马特鲁 Matruh",
                        sub: [{name: "地级市、县"}, {name: "马特鲁 Matruh"}],
                        type: 0
                    },
                    {
                        name: "南西奈 Janub Sina",
                        sub: [{name: "地级市、县"}, {name: "图尔 Janub Sina"}],
                        type: 0
                    },
                    {
                        name: "北西奈 Shamal Sina",
                        sub: [{name: "地级市、县"}, {name: "阿里什 Al `Arish"}],
                        type: 0
                    }],
                type: 1
            }
        ]

JSON数组