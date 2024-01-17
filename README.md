## Comparison of Speech to Text APIs
| Service                    | Latency             | Observation                                                                                             |
| -------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------- |
| **Deepgram (Remote File)** | 1 to 2 seconds      | Last few words are not transcribed                                                                      |
| **Deepgram (Local File)**  | 2 to 3 seconds      | Last few words are not transcribed                                                                      |
| **OpenAI Whisper**         | 2.5 to 3.25 seconds | Complete & accuratetranscription                                                                        |
| **AWS Transcribe**         | 10.5 to 11 seconds  | Complete & accurate transcription                                                                       |
| **Google Cloud**           | 5.75 to 6.5 seconds | Few words weren't properly transcribed. Accuracy depends on the type of model used & sampling rate, etc |


### Setup Details
* File Used - https://cdn-lankesh002-dev.enparadigmtech.com/roleplay/user_response_audio/1705473842647_52721_Sample_30_sec_english.mp3
* File Size - 413 KB
* File Duration - 30 seconds
* Actual Transcription
    ```
    ```

## DeepGram

### Remote File
```bash
python3 deepgram_remote_file.py
Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the, traction that is getting to his shared URL. Please

Time elapsed:  1.74  seconds

Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the traction that is getting to his shared URL. Please

Time elapsed:  1.29  seconds

Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the traction that is getting to his shared URL. Please

Time elapsed:  1.03  seconds

Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the, traction that is getting to his shared URL. Please

Time elapsed:  1.23  seconds

Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the traction that is getting to his shared URL. Please

Time elapsed:  1.58  seconds

Average time:  1.37  seconds
```

> FINAL RESULT: 1 to 2 seconds

### Local File
```bash
python3 deepgram_local_file.py
Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the traction that is getting to his shared URL. Please

Time elapsed:  2.7  seconds

Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the traction that is getting to his shared URL. Please

Time elapsed:  2.38  seconds

Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the traction that is getting to his shared URL. Please

Time elapsed:  2.13  seconds

Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the traction that is getting to his shared URL. Please

Time elapsed:  2.5  seconds

Transcription:  Hi there. I'm building a software, and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL. And the original poster of that content, should be able to see all the comments that he received on the URL, and he should also be able to see the, traction that is getting to his shared URL. Please

Time elapsed:  2.29  seconds

Average time:  2.4  seconds
```

> FINAL RESULT: 2 to 3 seconds

## OpenAI Whisper
> OpenAI AI Transcribe API expects file objects. Hence, to make it work with remote files, we need to download the file first and then pass it to the API. References [community discussion](https://community.openai.com/t/whisper-can-we-transcribe-from-url-and-file-upload/95700) and [documentation](https://platform.openai.com/docs/api-reference/audio/createTranscription).

### Local File
```bash
python3 openai_local_file.py
Transcription:  Hi there, I am building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the traction that is getting to his shared URL. Please provide that.


Time elapsed:  3.63  seconds

Transcription:  Hi there, I am building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the traction that is getting to his shared URL. Please provide that.


Time elapsed:  2.32  seconds

Transcription:  Hi there, I am building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the traction that is getting to his shared URL. Please provide that.


Time elapsed:  2.64  seconds

Transcription:  Hi there, I am building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the traction that is getting to his shared URL. Please provide that.


Time elapsed:  3.2  seconds

Transcription:  Hi there, I am building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the traction that is getting to his shared URL. Please provide that.


Time elapsed:  3.11  seconds

Average time:  2.98  seconds
```

> FINAL RESULT: 2.5 to 3.25 seconds

*NOTE** - Providing the `language` information to the API, would slightly improve the latency & performance. However, it is not a significant improvement.

## AWS Transcribe
```bash
python3 aws_transcribe.py
Transcription:  https://s3.ap-south-1.amazonaws.com/aws-transcribe-ap-south-1-prod/223865955266/transcription-1705479472/86fb7696-ab90-409d-aca0-4f14f6e78a13/asrOutput.json?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCmFwLXNvdXRoLTEiRjBEAiB%2BRXM%2Fm%2F2aOQZTPa%2BDT7wwvPEA2gzrpxMnW8Ig5FtROwIgdF89UOB61d9%2BftnEJETDR2gThkzsHh40lWPMVuro4AEqyAUIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgw2NjMwMTkxMTk4MzYiDPRO2uYGrTEOYmExkiqcBb0gaeBS1PqHOmD5NQyjQBi9Js%2FB70ZcxRTN24gpQ9YY5Rh7vdlyX9D5tXvD0i1VGnkASwvQafglXvDKJNF2MJ7o%2BkyzTHDpsqpnDTLnm8BpR8%2BVshzskb2AWsQeo7AFm%2BtSxPlk3fyGPlQIdhyqXX1X6DMJaTR1h2J4CdJy2V7ph1DNSI%2BF5ajrlb3rbomFk6wQ%2FQY3Win9C4JqCw2PruPEnxxJc3mxh9Tn2lkYrmBtSA%2Fqp8kVEToNCzxS1xXdY30xpDbQG4pgQYPpj11vKxSHikteKOLDWODhotVTcgzB4n078d3w40%2FxMLyTl9UPT%2Fo1jJ85lIVkw9690OPxzLzsLlSaryrAJcWAh9k%2Blh9g2ORT5zu2hadRMKyECZWTsRhlnCS%2FEocx324p4orApUL%2FT7EbDs%2FhXsB%2FAK7fr2a4Zk7sv3mmMXnXoZU1dmA1BUQKZcrz%2FLT95gDcsDMjG5Z0uhzKO0ElFpk9L9aPCsXvBxbbmNoYNgAZr1Z5csi9vGYXOHYcVexZBWzpOVhUfkeqkvAC5XX453JL4pnChwm%2FwVo8KqoyYLZ3zdb%2FCqnbU%2FfY%2BwzxahW8GbCXcmf%2BJCLtdlWsXypX92oKk%2FXrAkEsblLIg0%2BGqwPdgKep%2BrtCu6nI%2FXQldyXb9c%2F0y7FhjdDY8HPLKTurgkJ5snrDm3G%2FxotJM3apxyFEfgO3EleAc7aSeFIqXd6qcl42qnDjvT8aINYGaGyuKwU5GfiXJtvIp%2Bd4PA%2FSfTDoeEOUWIXqegtYM8H4i95fQ5jlRFr3iAZnh2%2F5Z%2FHHs%2Bj%2BvKSm8NUP10KIOHIv50eHbezLifZFXVxU%2Bq9PeoiuZqdj6RQ94cC4G96uNNpwzqBQi1DPBDtxVIOuKyH0OVX0GoaHMKv%2Bna0GOrIBAKkPgx1vYskIELQYdhdxWM%2FIMo%2Fj5ZzTWORBhxnEkSt5dSwdD%2FNO3vUlYybgldd0bocCdZihS53iUla0LIP9RpzIG2bdFFV4XnOOCXIFK5Z0KW%2F0dW8tPgwLRjrDnIMicRFr4gDF%2BLFTGAg2ecp%2BdxZbHEiKovsEJLInu3uphica5TMCyomMECXV7PlNUBpxeBT9IzsJTXvu0ZPmQRkKpdjkX%2Fns9hESgrORI8cC7s4QSQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240117T081803Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=ASIAZUXYE4TOOIOR4J46%2F20240117%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=1ca75508b2c3e890b098bcdaa01ae55cfa2dc8bc1f43070be3ad2214829e4117

Time elapsed:  10.75  seconds

Transcription:  https://s3.ap-south-1.amazonaws.com/aws-transcribe-ap-south-1-prod/223865955266/transcription-1705479483/fd2ff5b8-3b89-4d50-b27f-59ef73a4f6c2/asrOutput.json?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCmFwLXNvdXRoLTEiRjBEAiARQQbGFJZ7PA5%2BTH6L%2Fl6%2Fp2OBuqPId2%2B5F5CLr84XbgIgYWtI5Au4vDi%2Bf9dTA1uqrMd9ElGiUmZbv4koLVD0WiMqyAUIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgw2NjMwMTkxMTk4MzYiDPfzYAMt4Sjx1ClHACqcBW%2BvclW5QG6vito4d66hfzkdNKAuW5qOLqZExf23OeynXWjU2rBNv7peFiEB9NpTP3F58yninYuf1u1oP3n5CoonG7xwfJ%2BNI9Z9iTlLEid4LqU06AJ1vplyEa0iGVGnSGrziaqugd0vuBUYL8tSx0h99l0hIjOvIphyquYocScbja80P%2Fjm7TqHfI00uRql0sF%2F6%2FdMuK2b%2FVO8ZkRBN1yAXvtKHaI9PVvZkM9BwjfwkVjh0X7a1eRTk%2BG5CJE%2B4Q5l2cCqpxgjbxG5Faq41aKNqLm6BMaj3gkJyShMuCZAUjkymgZdom8pZVN1Vh%2Blz5BuMDmueLUnBcwoL8yEnHqtfjvp3hSqXlV%2FuDVmfvs0pvMFLAggaDKMgTknOGmT5WPNhBCgKUelklc48Kj%2FCcXkozj9Nz%2FdaSgt%2BvhWORMWlQGjKMCEoy8G8u7nDXDlI87%2F1aKCnC8gndeElvabIOtPFlSlz48M8f97DeOcSB7vXGLLktimbsFxfYv5OOMaubm6HMo2pwbQ3f74CcJyBMiCjoINXLHkZgasuGSJYO406%2FtJn2RCTGCKpviYHz25zU454d1A7fbuKkuetjNX%2FWzRI9nilcVefj7yzoYpRRsRiag%2F%2FTSKtkTNDkKNJ49huEz6RxxlIA6hPsJWbcmMeZiFZ%2BjytNGJqYJcUf96C6XLrfFlEtbn%2F3mX%2Buu3L85ATHt4GveDjSMXN0gkZJnxHfhTtm2CGYnDfC1bo5ETAbtoVBzT9RrA3OYpw4n8UnCLOq0Be7rrN2I1X6bf%2BUbBBf8YPp38GbSBz2%2FGBdb144aloi1EU1LOAgqxnnED1ye8I7WvsI15UftpUbqX1nBchYNd1Vvosh%2FrQEgxmvfjzuKp0YV4wTiApGcPum4OMKGEnq0GOrIBCs%2FGx3yo8nRqxudlSPGsM7h5NbZl%2F5pwrIQo3D6k65c%2F5eCMGL3ppzciXhHzKpBdoDmXsBohsrP20FMlgv5FO8pJ6t%2B3OSBJCAENIfIHzW9pqFuF34rtIJjzb9Xihlxv%2BX2f8A%2B4D9nTMHVeDhVFb4iBKzgBOLLfqbfZGVCUt8P86tYJrHVHfzWQis3uEofcAW%2Fcs0hkNHPZs1IoaHezS8kF6nXiwJHeWE72ZBtu47c%2Fog%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240117T081813Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=ASIAZUXYE4TOJJ6RD6UZ%2F20240117%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=701d9242245b047ec13cc228516046546f00ceaac332ceeddeda69527e675859

Time elapsed:  10.37  seconds

Transcription:  https://s3.ap-south-1.amazonaws.com/aws-transcribe-ap-south-1-prod/223865955266/transcription-1705479493/22420c72-5880-4e6e-9be3-3291ef67a85c/asrOutput.json?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCmFwLXNvdXRoLTEiRjBEAiARQQbGFJZ7PA5%2BTH6L%2Fl6%2Fp2OBuqPId2%2B5F5CLr84XbgIgYWtI5Au4vDi%2Bf9dTA1uqrMd9ElGiUmZbv4koLVD0WiMqyAUIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgw2NjMwMTkxMTk4MzYiDPfzYAMt4Sjx1ClHACqcBW%2BvclW5QG6vito4d66hfzkdNKAuW5qOLqZExf23OeynXWjU2rBNv7peFiEB9NpTP3F58yninYuf1u1oP3n5CoonG7xwfJ%2BNI9Z9iTlLEid4LqU06AJ1vplyEa0iGVGnSGrziaqugd0vuBUYL8tSx0h99l0hIjOvIphyquYocScbja80P%2Fjm7TqHfI00uRql0sF%2F6%2FdMuK2b%2FVO8ZkRBN1yAXvtKHaI9PVvZkM9BwjfwkVjh0X7a1eRTk%2BG5CJE%2B4Q5l2cCqpxgjbxG5Faq41aKNqLm6BMaj3gkJyShMuCZAUjkymgZdom8pZVN1Vh%2Blz5BuMDmueLUnBcwoL8yEnHqtfjvp3hSqXlV%2FuDVmfvs0pvMFLAggaDKMgTknOGmT5WPNhBCgKUelklc48Kj%2FCcXkozj9Nz%2FdaSgt%2BvhWORMWlQGjKMCEoy8G8u7nDXDlI87%2F1aKCnC8gndeElvabIOtPFlSlz48M8f97DeOcSB7vXGLLktimbsFxfYv5OOMaubm6HMo2pwbQ3f74CcJyBMiCjoINXLHkZgasuGSJYO406%2FtJn2RCTGCKpviYHz25zU454d1A7fbuKkuetjNX%2FWzRI9nilcVefj7yzoYpRRsRiag%2F%2FTSKtkTNDkKNJ49huEz6RxxlIA6hPsJWbcmMeZiFZ%2BjytNGJqYJcUf96C6XLrfFlEtbn%2F3mX%2Buu3L85ATHt4GveDjSMXN0gkZJnxHfhTtm2CGYnDfC1bo5ETAbtoVBzT9RrA3OYpw4n8UnCLOq0Be7rrN2I1X6bf%2BUbBBf8YPp38GbSBz2%2FGBdb144aloi1EU1LOAgqxnnED1ye8I7WvsI15UftpUbqX1nBchYNd1Vvosh%2FrQEgxmvfjzuKp0YV4wTiApGcPum4OMKGEnq0GOrIBCs%2FGx3yo8nRqxudlSPGsM7h5NbZl%2F5pwrIQo3D6k65c%2F5eCMGL3ppzciXhHzKpBdoDmXsBohsrP20FMlgv5FO8pJ6t%2B3OSBJCAENIfIHzW9pqFuF34rtIJjzb9Xihlxv%2BX2f8A%2B4D9nTMHVeDhVFb4iBKzgBOLLfqbfZGVCUt8P86tYJrHVHfzWQis3uEofcAW%2Fcs0hkNHPZs1IoaHezS8kF6nXiwJHeWE72ZBtu47c%2Fog%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240117T081824Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=ASIAZUXYE4TOJJ6RD6UZ%2F20240117%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=139afe9f1ed72c90e7c805930f7ca825f5cfbcac81a7a6eeb01a1bc5be92ab11

Time elapsed:  10.37  seconds

Transcription:  https://s3.ap-south-1.amazonaws.com/aws-transcribe-ap-south-1-prod/223865955266/transcription-1705479504/279026f1-d5de-4af7-8c1e-ea456c2bae7d/asrOutput.json?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCmFwLXNvdXRoLTEiSDBGAiEA9w6Hsaql6x55NJkfuM%2Fj0VwmZhcMSSa4ngNgBtQppUACIQCJ9EiLf6pxuQQG5am8ndBoWC4GeDkGDEbyKjF0R21GsCrHBQi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAMaDDY2MzAxOTExOTgzNiIMSU9pewAELmVmo3NMKpsFAkpb9lY2CPIe3Knx%2FiWTjUqbiBrB6WU0rZzf484%2Fmy4dFZkllxaE6Ud%2Bi3xNCbjocW1lQHHtPzi56B7DZNKgA2Hpwhpf3YUUov3MmU5tPfDLQ8OsruuOiWAuhef2mZihi0NfH%2BmCc%2FzDgxwxCJ6QyKZsW7n9ZTtL7RLMMStUcrR3X35BNraUe3Dbli%2FmLRQu%2Bxh7%2BaLd0PT63SFqtmaiapK%2FS0fJVDzEwjxrXPb3NEaMiBN%2FU5Uevge%2BW%2FU2aCVfgXCsFOnTL1RAjxp49q%2BVveE2oNdpg1NYdriQPJdyvB0QH9XFhcQA00%2FWI%2FqUf0A0gUfYWqgWnmD9o9e7nuCsXxU%2F7xMgS3eIdNhLKuEG0qFWCukOfOk%2BLKC09ZI3s7cEqvyawPLTLxR38Yl6acrbmq0AmyKCmljceSqr%2F0MmIA6pKO1HkCq086wQ6rhd8SCNQMtidIWGufX6EjzfegqaBnbfQd2JpHpXCbvCdJVYF0FxnW1E7id0pd5IR162wswwmaHA6eBDD3tV3ic9kLq3G6zasLm8pkubiYF20IMyxmBgOqCA5kBGos6UnG8Dh7K1HMnrbgQ9udhrOtNA0trDXVf1cEmwF1y1XISHyssRz%2BfSDoGrpzTVN8op%2BslIPviwq6V1ETS7sT4cBo9%2BdpmR%2FjeBn3DYdRSHJoPL9m7QYNvMl2WhCJiTrEo8S%2Bevwp5aFmJQDfkwO%2BaqmkGb46Q0%2B7kdwo18lf3qSP5hZwfb627QImMHFLd12HKRxVC7H0v4ZDNM469CP3CrjUzpzqWb%2FV73wOqy%2Ba37bOJLDt4FigJFynA5VUL6rSzZ0WX0k3EJ%2FwuIxq3cdXWVHUJdrBib2cQNYgr4%2Fv%2Bx1VeaNXerH6%2Fnb3Luczi5NC4nqDDN%2F52tBjqwAcjf4ajOdMZeKpHsxIibmv6q0IY9q7xlS1b1HbQmyTBgHzVgfxr%2BHAA%2FM4aQ9HHpZziuvLAWLk94OocsE66mhV13jJA%2BR%2BUqxriVT7sScDNlkN70Iv3HMzYAwDnbPXg3gO8w1F3Z7OaCRCdNC%2BwmvPhb5t3LQJClQU3lQomV2zshCjfxwijlsCOy6OT57BxscN7pZcu9ODdfsmdSFNUEECZf6yj5kWPXjWXNAeDeKPOk&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240117T081834Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=ASIAZUXYE4TOPRMFA6OX%2F20240117%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=9ec8535d434167b7dc1558757919cdf5a741781aa5d3a9b16d5f24623d922d07

Time elapsed:  10.43  seconds

Transcription:  https://s3.ap-south-1.amazonaws.com/aws-transcribe-ap-south-1-prod/223865955266/transcription-1705479514/92ee06c4-a318-4b1a-ba2d-7eaae18bc275/asrOutput.json?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCmFwLXNvdXRoLTEiRjBEAiBqmdHXihCN8Yy7SQCBL%2F5Ei7ZZAQBTiHLorilFIIo0tgIgf8idncjgK62GV%2BqoELFrvjtLUgZwyT%2BItMM8Vg9FpFAqyAUIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgw2NjMwMTkxMTk4MzYiDHTU4q5FDY6tI1V3%2FiqcBcDjJGrS5FpwHZFJ0OzKNvEgBV5IZRH4PxCDwy4IzlhJBad39OPGaXDW3fQZxYc79I3CobDrzscg6tF4DztRpiUdoIVYDnPOUknfjn9D%2FrPpW1XwUdCmRz24Ot2ZQ%2BoYYiUI7QLki03vX6uETwZfknTP7ePiwqXn9h9i4Ci8gHYdC1Cm%2F%2Fyp98JGRXrpVbfVR4MhbJLBpbCXBm3FmmwOnXqJYcgiEnBC2N0RpZypMuteLYJF3WhUp5gaGgM49kEw%2BXMFX15dd%2BJF3nn7zraZRICEDsoiYznx9wDQ4JnTSXw3Lopbjb1JuNf2fwxVuanHrrp548x1aRrvOWejAGKjK%2BAGtRznsu0kTNd%2Bzk5WsK0CH6ZYEvFF7ITmUg1RMvhV3dIsRqU8i7%2Bq3DkswnGUMb%2FCE%2BtL0E%2FloLtpDFtk0OeGfW%2BGQ35PsVcfMF49BwT2NHS0vNWEBLQrAX%2FCcCbkpXh2OR2dk%2F1v60dIBwOhqZwbzEKMjxc77cQ26dRrxj54sqTdUTKJNyGRX4HKDCaw0lWzYIUDfVaO6SvKGQ8Xt8j%2Fe2kZZAmZ8jAVXxo3a5tUxBzHXBQ%2F%2BFC8M2aijMvbn7q1fJLjkhWs0pmmF%2BGQRZF8952XCfHO1JztAarf4dpmfa6%2BwWbpGrsV2xAzJTgO3G0nPhxoAmIURhzQfGcpgn%2FF87Wale3rLndTigTjW588ANjctIh7CM06EmYwUtmSbGid181j%2B8ZuZCn1iIW65EM7dN%2BtJaUB3MyqSPYiytjDyVuky4xoh7P03p9IsSR4MwP0ZuulsmT%2F0NWW%2Bas43JVkOW%2FSKWRsLOmEnWUecikdl6a10v2MTfjmLoNzucs7hZcPPx7DjBQ04oHFzQTZy5%2BlUKKxq3GxAwjWocBcMPOGnq0GOrIB%2Fv6X1%2FIIVBtKeka0ZVbm2msilpLifNuU%2Fk9jMzJhsmaqeVyDgoLTXqvUAFQ7KdBEIqZkdahDWUdeUIvKGv2pzkQ6fOV2w247WQtLfbdXork5JIqQwHOaqmwDv0oFpW%2B0YJMyKihTlGxR7JaOAz1UEtV4o2YYyMuWzycKJ%2BnvMPaz6qsLygy4dh5CJon4WiioBe6aBF9mlD2UAreAHcqKDVDYlnnUe7SEtTVQkHQ3%2BK4IjQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240117T081845Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=ASIAZUXYE4TOD66UMVT4%2F20240117%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=b8d8315396cc01acc32a1d8d3f7af3d7ce805cfa7287ba7433bb3728c74d2840

Time elapsed:  10.29  seconds

Average time:  10.44  seconds
```

**Points to Note**
* AWS Transcribe processes audio files asynchronously. We start a transcription job and then periodically check for its completion. This is why there's a `time.sleep(0.5)` in the script. The sleep duration is a balance between checking too frequently and waiting too long.
* AWS Transcribe requires the audio file to be accessible from an S3 bucket.
* AWS Transcribe stores the transcription results in a JSON file in the same S3 bucket. We need to download this file and parse it to get the transcription text.

**Actual Transcription**
```text
"Hi there, I am building a software and I would like to have features which provide the user the ability to share content via any of the social media. And also be able to comment on the fly on the same URL. And the original uh poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the traction that is getting to his shared URL. Please provide that."
```

> FINAL RESULT: 10.5 seconds

## Google Speech-to-Text
> The transcription result varies based on the model used. [Documentation](https://cloud.google.com/speech-to-text/docs/transcription-model)

```bash
python3 google_speech_to_text_local_file.py
hi there I'm building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original. uh poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the uh traction that is getting to his shared URL. please provide that


Time elapsed:  6.17  seconds

hi there I'm building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original. uh poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the uh traction that is getting to his shared URL. please provide that


Time elapsed:  6.35  seconds

hi there I'm building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original. uh poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the uh traction that is getting to his shared URL. please provide that


Time elapsed:  6.24  seconds

hi there I'm building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original. uh poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the uh traction that is getting to his shared URL. please provide that


Time elapsed:  6.72  seconds

hi there I'm building a software and I would like to have features which provide the user the ability to share content via any of the social media and also be able to comment on the fly on the same URL and the original. uh poster of that content should be able to see all the comments that he received on the URL and he should also be able to see the uh traction that is getting to his shared URL. please provide that


Time elapsed:  5.99  seconds

Average time:  6.29  seconds
```

> FINAL RESULT: 5.75 to 6.5 seconds