import cv2
import numpy as np

ramp = '@#MBHA$Gh93X25Sisr;:,.'
ramp_numpy = np.array(list(ramp))


class ASCIIConverter:
    @staticmethod
    def build_ascii(indices):
        res = ramp_numpy[indices]
        s = ''
        h = indices.shape[0]
        for i in range(h):
            s += ''.join(res[i].tolist()) + '\n'
        return s

    def convert_img_to_ascii(self, img, sampling_step='auto', aspect=2,
                             norm_style='mean', eq_hist_flg=True):
        sampling_step = img.shape[0] // 128 \
            if sampling_step == 'auto' \
            else int(sampling_step)

        if img.ndim == 3:
            if norm_style == 'mean':
                img = np.mean(img, axis=2)
            elif norm_style == 'gray':
                img = (.2126 * img[:, :, 0] + .7152
                       * img[:, :, 1] + .0722
                       * img[:, :, 2])
            else:
                raise Exception('Неизвестный формат: {}'
                                .format(norm_style))

        if eq_hist_flg:
            img = cv2.equalizeHist(img.astype(np.uint8))

        src_height, src_width = img.shape[:2]
        dst_height, dst_width = (int(src_height / sampling_step / aspect),
                                 int(src_width / sampling_step))

        indices = np.zeros((dst_height, dst_width),
                           dtype=np.float32)
        step_h, step_w = (int(sampling_step * aspect),
                          sampling_step)
        for j in range(step_h):
            for k in range(step_w):
                indices += (
                               img)[j:j + step_h * dst_height:
                                    step_h, k:k + step_w * dst_width: step_w]

        indices = ((indices / (step_h * step_w) / 256 * len(ramp))
                   .astype(np.uint32))
        return self.build_ascii(indices)
